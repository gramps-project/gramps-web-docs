# Lists

Every object type in Gramps Web has a list view: People, Families, Events, Places, Sources, Citations, Repositories, Notes, and Media. They all work the same way and share the same tools for sorting, filtering, and editing in bulk.

## Sorting and paging

Click a column header to sort by that column; click it again to reverse the order. Sorting is performed by the server, so it applies to the whole list, not just the page you are looking at.

Long lists are split into pages. Use the pagination controls at the bottom to move between them.

On narrow screens the table automatically switches to a compact layout, so list views remain usable on a phone.

## Choosing columns

Click the gear icon above the list to open the **Columns** dialog. Tick or untick a column to show or hide it. **Reset** restores the default selection for that list.

At least one column must remain visible, so the last remaining column cannot be unticked.

Your column selection is remembered per object type and per family tree. It is stored in your browser, so it is not visible to other users – but it also does not follow you to a different browser or device.

## Filtering

Click the **filter** button to open the filter panel. A pill toggle at the top of the panel switches between two modes:

- **simple** – a set of ready-made filters that depend on the object type. For people, for instance, you can filter by birth year, death year, various person properties, the number of associations, tags, and whether an object is private or public.
- **GQL** – a single text field for an advanced query in the [Gramps Query Language](gql.md). Type the query and press Enter or click **Apply**. If the query is invalid, the field's frame turns red.

Active filters are shown as chips above the list. Remove a single filter by clicking the chip's clear button, or use **Clear all filters** to remove them all at once.

!!! note
    The two modes are alternatives, not additive: a GQL query replaces the simple filters, and switching back to simple mode drops the query.

## Selecting objects and acting on them in bulk

Users with edit permissions see a **Select** button next to the filter button. Click it to enter selection mode, which adds a checkbox to every row.

Tick the objects you want, and a toolbar appears showing how many are selected, along with an **Action** dropdown and an **Apply** button.

### Delete

Select one or more objects, choose **Delete**, and click **Apply**. A confirmation dialog asks you to confirm, warning that the action cannot be undone.

!!! tip
    Deletions are recorded in the [revision history](revisions.md) like any other change, so a mistaken bulk delete can be reversed by undoing the corresponding transaction.

### Merge

Select **exactly two** objects, choose **Merge**, and click **Apply**. A dialog asks which of the two should provide the primary data for the merged object; click the one you want to keep as primary. The other object's data is merged into it and references are updated.

Merging is available for people, families, events, places, sources, and citations. It is not available for repositories, notes, and media objects.

If you choose an action without a valid selection – for example a merge with only one object selected – a dialog explains what is required.
