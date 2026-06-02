# Theming and appearance

The Gramps Web frontend ships with a light and a dark theme and lets you choose an accent color. This
page explains how the theming system is built and how to go further — custom surface colors, fonts, or
a fully bespoke palette — by overriding the frontend's design tokens with a small custom stylesheet.

!!! note
    The design tokens described below are the frontend's internal theming variables. The accent-color
    setting is a stable, supported feature; the deeper token overrides are an advanced surface that may
    change between major frontend releases, so re-test custom themes after upgrading.

## How appearance is built

The frontend ([grampsjs](https://github.com/gramps-project/gramps-web)) is a [Lit](https://lit.dev/)
application: most components render inside their own **Shadow DOM**. Ordinary CSS selectors cannot
reach inside a shadow root, but **CSS custom properties (variables) inherit through shadow boundaries** —
and the theme is built entirely on custom properties.

Colors flow from one layer of **Material Design 3 system tokens**:

```
--md-sys-color-primary, --md-sys-color-on-primary,
--md-sys-color-background, --md-sys-color-surface,
--md-sys-color-surface-container-lowest … -low … (container) … -high … -highest,
--md-sys-color-on-surface, --md-sys-color-secondary,
--md-sys-color-outline, --md-sys-color-outline-variant, --md-sys-color-error, …
```

At runtime these are generated from a single **seed (the accent color)** using
[material-color-utilities](https://github.com/material-foundation/material-color-utilities) and written
as inline properties on the document. Everything else is defined in terms of them — in `global.css`
you can see the Material Web Components (`--mdc-theme-*`), Web Awesome (`--wa-color-*`), and grampsjs
(`--grampsjs-*`) variables all referencing the `--md-sys-color-*` tokens. So there is effectively one
place to change a color, and it cascades everywhere.

## Changing the accent color

If you only want a different accent/brand color, set the frontend's primary color. The full palette —
including light/dark variants and contrast — is regenerated from it, so buttons, links, the app bar,
active navigation, and FABs all follow. This is the supported, upgrade-safe path and is all most
instances need.

## Custom theming with CSS

To customize surfaces, fonts, or the whole palette, override the tokens with your own stylesheet.

Because the runtime writes the `--md-sys-color-*` tokens as **inline** properties (without
`!important`), an author stylesheet that declares them **`!important`** wins the cascade, and — being
custom properties — the values inherit into every shadow root. Declare them on **`html, body`** so the
rule matches whichever element the runtime writes to:

```css
html, body {
  --md-sys-color-primary:         #8c2f24 !important;   /* accent  */
  --md-sys-color-on-primary:      #f7ece8 !important;
  --md-sys-color-background:      #f4efe6 !important;    /* page    */
  --md-sys-color-surface:         #fbf8f1 !important;    /* cards   */
  --md-sys-color-on-surface:      #231d17 !important;    /* text    */
  --md-sys-color-outline:         #c4b69c !important;
  --md-sys-color-outline-variant: #ddd3c0 !important;
}
```

### Map the surface ramp, don't flatten it

Material components use the container ramp (`surface-container-lowest` → `-low` → `-container` →
`-high` → `-highest`) for elevation, hover, and raised states (menus, dialogs, cards, the app bar). If
you set them all to one value the UI loses its depth. Map a light-to-slightly-darker range onto the
ramp instead:

```css
html, body {
  --md-sys-color-surface-container-lowest:  #fffdf8 !important;
  --md-sys-color-surface-container-low:     #fbf8f1 !important;
  --md-sys-color-surface-container:         #f4efe6 !important;
  --md-sys-color-surface-container-high:    #ece5d8 !important;
  --md-sys-color-surface-container-highest: #e3d9c7 !important;
}
```

### Fonts

grampsjs exposes font tokens; set them and load the webfont yourself:

```css
@import url("https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&display=swap");
html, body {
  --grampsjs-body-font-family: "IBM Plex Sans", system-ui, sans-serif !important;
  --grampsjs-body-font-size: 16px !important;
  --grampsjs-body-font-weight: 400 !important;
}
```

### Light vs. dark

The frontend has both a light and a dark palette. If you override only some tokens, a user in the
other mode gets a half-themed result. Either pin your instance to one mode, or provide values for both
(for example inside a `@media (prefers-color-scheme: dark)` block).

### Things the tokens don't reach

A few elements use fixed colors instead of the M3 tokens:

- the sex/gender chips — `--color-boy`, `--color-girl`, `--color-unknown`, `--color-other` (these are
  CSS variables too, so they can be overridden the same way);
- map tiles/markers (Leaflet/MapLibre) and some chart/visualization colors, which are set in component
  logic or tile imagery rather than by the theme tokens.

## Where to put the custom CSS

There is currently no `config.js` option for custom CSS, so the stylesheet must be linked from the
served frontend (static files in the image's `static/` directory). For a Docker deployment:

1. Put the overrides in a file, e.g. `custom-theme.css`, and mount it into the static directory:

    ```yaml
    volumes:
      - ./custom-theme.css:/app/static/custom-theme.css:ro
    ```

2. Add a `<link rel="stylesheet" href="custom-theme.css">` just before `</head>` in `index.html`.
   **Do not mount a pinned copy of `index.html`** — the JS bundle filenames are content-hashed and
   change on every upgrade, so a stale `index.html` would reference missing bundles. Instead insert the
   link idempotently at container start, for example:

    ```sh
    grep -q custom-theme.css /app/static/index.html \
      || sed -i 's#</head>#<link rel="stylesheet" href="custom-theme.css"></head>#' /app/static/index.html
    ```

A service worker caches the static assets, so after changing the CSS do a hard reload (or rename the
file) to bypass the cache.
