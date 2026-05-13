# Map

The Map page displays all places in your family tree as interactive markers on a geographic map. It is accessible from the sidebar.

## Place markers

Only places that have GPS coordinates stored in the Gramps database are shown on the map. Places without coordinates are silently omitted. GPS coordinates can be set on the place detail page (edit the place and fill in the latitude and longitude fields).

!!! tip
    If many of your places are missing from the map, open a place detail page and check whether latitude and longitude are set. You can add or correct coordinates directly from the place's edit view.

Each place with coordinates is shown as a marker. Clicking a marker opens a summary card showing the place name and its linked events and people. Click the place name in the card to open the full place detail page.

## Search

The search box in the top-left corner of the map lets you jump to any location in the world by name. This does not filter the tree's places – it simply pans and zooms the map to the searched location.

## Time slider

The time slider at the bottom of the page filters which place markers are shown based on the year of their associated events:

- Drag the handle to select a year.
- Only places linked to events that fall within the selected time window are shown.
- Use this to trace where your ancestors lived at a particular point in history.

## Map layers

A layer switcher button (stacked-layers icon, bottom-left) lets you choose between two base maps:

### Base Map

The default layer, powered by [OpenFreeMap](https://openfreemap.org) (Liberty style for light mode, dark style for dark mode). This is a modern general-purpose map suitable for locating places.

### Historical Map

Switches the base map to [OpenHistoricalMap](https://www.openhistoricalmap.org) (OHM), a community-driven project that maps the world as it existed at different points in time – think of it as a historical counterpart to OpenStreetMap.

When the Historical Map layer is active, the time slider also filters the map tiles themselves: OHM renders the map as it appeared in the selected year, so historical borders, place names, and features are shown instead of the modern ones. This makes it possible to see both your ancestor's location and the contemporary geographic and political context in a single view.

!!! note
    OpenHistoricalMap coverage varies by region and period. Areas or eras with sparse contributions may show limited historical detail. If you notice missing or inaccurate historical data, consider [contributing to OpenHistoricalMap](https://www.openhistoricalmap.org) – it is an open community project that anyone can edit.
