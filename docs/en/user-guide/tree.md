# Family Tree

The Family Tree page is accessible from the sidebar and displays interactive charts centred on a selected person. Five chart types are available via tabs at the top of the page.

## Selecting the starting person

All charts start from the person currently selected in the tree (shown in the toolbar). The currently centred person is highlighted with a drop shadow. Use the **Home Person** button to jump back to your home person, or the **Back** button to return to the previously viewed person. Clicking a person's card in any chart re-centres the chart on that person.

If no home person has been set, the page will prompt you to go to the home page and set one.

## Chart types

### Ancestor Tree

A pedigree chart showing the ancestors of the selected person. Parents appear to the left (or right, depending on layout), grandparents further out, and so on.

### Descendant Tree

Shows the descendants of the selected person – children, grandchildren, and so on.

### Hourglass Graph

Combines ancestors above and descendants below the selected person in a single view.

### Relationship Graph

Shows the relationship path between two people. The selected person is one endpoint; click any other person in the chart to set the second endpoint and display the shortest relationship path between them.

!!! note
    The same person may appear more than once in the graph – for example when someone has been married multiple times and appears in several family units along the path. This is intentional, not a bug.

### Fan Chart

A circular pedigree chart. Ancestors radiate outward from the selected person at the centre.

## Navigation controls

All chart types share a toolbar with the following buttons:

- **Home Person** – jump back to your home person
- **Back** – go back to the previously centred person
- **Person Details** – open the full profile page of the currently centred person
- **Preferences** – open a dialog to adjust chart-specific display options (see below)

All charts support **pan** (click and drag) and **zoom** (scroll wheel or pinch).

## Chart preferences

The **Preferences** dialog (gear icon in the toolbar) lets you adjust the following options, depending on the chart type:

- **Max Ancestor Generations** – how many generations of ancestors to display
- **Max Descendant Generations** – how many generations of descendants to display
- **Max Degree of Separation** – for the Relationship Graph, the maximum path length to search
- **Max Number of Images displayed** – limits profile photos shown in the chart for performance
- **Name Display Format** – controls how names are shown on person cards

Click **Reset** to restore the defaults, or **Close** to apply your changes.

Chart preference settings are stored in the browser's local storage, so they persist across sessions on the same device.

## Default chart type

The chart type shown when you first open the Family Tree page can be configured in [User Settings](settings.md). Your chosen default applies on all your devices.

## Editing the tree

Users with the Editor role or above can add and link people directly from the Ancestor Tree. See [Editing the family tree](tree-edit.md) for details.

