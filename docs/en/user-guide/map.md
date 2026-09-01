# Map

The Map page displays all places in your family tree as interactive markers on a geographic map. It is accessible from the sidebar.

## Place markers

Only places that have GPS coordinates stored in the Gramps database are shown on the map. Places without coordinates are silently omitted. GPS coordinates can be set on the place detail page (edit the place and fill in the latitude and longitude fields).

!!! tip
    If many of your places are missing from the map, open a place detail page and check whether latitude and longitude are set. You can add or correct coordinates directly from the place's edit view.

Each place with coordinates is shown as a marker. Clicking a marker opens a summary card showing the place name and its linked events and people. Click the place name in the card to open the full place detail page.

## Search

The search box in the top-left corner of the map searches as you type and groups the results under three headings:

- **Places** – places in your family tree. Selecting one pans the map to it and highlights its marker.
- **People** – people in your family tree. Selecting one switches the map into the person view described [below](#following-a-person-across-the-map).
- **External** – locations from [OpenStreetMap](https://www.openstreetmap.org/), for anywhere in the world. Selecting one simply pans and zooms the map to that location; it does not filter or change your tree's places.

The external results are also useful when adding coordinates to a place: you can look the location up here to see where it is before entering its latitude and longitude.

## Following a person across the map

Selecting a person – from the map's search box, or with the **Open in map** button on a person's detail page – shows the places connected to that person's events, joined by lines in chronological order. Small arrows along each line indicate the direction of travel, so you can follow a person's life from birth through to death across the map.

Places on a place detail page have an **Open in map** button as well, which opens the map centred on that place.

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

## Custom map overlays

In addition to the built-in base layers, you can turn any scanned historical map image – stored in Gramps as a **Media** object – into a custom overlay positioned on the live map. This is useful for scans of old city plans, parish maps, or property maps that you want to compare directly against modern or historical geography.

### Georeferencing an image

1. Open the media object for the scanned map image and switch to edit mode.
2. Open the "Map" tab and click **Edit coordinates**. This opens a georeferencing dialog with the image alongside a map.
3. Click **Select a point on the map**, then click the location on the map that a point on the image should correspond to. The image is placed on the map for the first time as soon as a point is selected.
4. Use the **Scale** slider to resize the image and the **Opacity** slider to see the base map through it while positioning.
5. Click **Align the image** and click on the map again to shift the image so that the pinned point lines up precisely.
6. Repeat the scale, opacity, and align steps until the image matches the underlying geography, then save.

Behind the scenes, this stores the image's corner coordinates in a `map:bounds` attribute on the media object.

### Viewing overlays on the Map page

Once a media object has been georeferenced this way, it automatically becomes available as a toggleable layer on the Map page. Open the layer switcher (stacked-layers icon, bottom-left) to show or hide each overlay independently of the base map. Overlays are listed by the media object's title.
