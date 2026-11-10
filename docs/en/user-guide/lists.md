# Lists

Every object type in Gramps Web has a list view: People, Families, Events, Places, Sources, Citations, Repositories, Notes, and Media. They all work the same way and share the same tools for sorting, filtering, and editing in bulk.

## Sorting and paging

Click a column header to sort by that column; click it again to reverse the order. Sorting is performed by the server, so it applies to the whole list, not just the page you are looking at.

Long lists are split into pages. Use the pagination controls at the bottom to move between them.

On narrow screens the table automatically switches to a compact layout, so list views remain usable on a phone.

## Choosing columns

Click the gear icon at the right end of the toolbar above the list to open the **Columns** dialog. Tick or untick a column to show or hide it. **Reset** restores the default selection for that list.

At least one column must remain visible, so the last remaining column cannot be unticked.

Your column selection is remembered per object type and per family tree. It is stored in your browser, so it is not visible to other users – but it also does not follow you to a different browser or device.

## Filtering

Click the **filter** button to open the filter panel. It offers three ways to filter, which can be combined:

- **Ready-made filters** in collapsible sections that depend on the object type. For people, for instance, you can filter by name, birth year, death year, various person properties, the number of associations, tags, and whether an object is private or public. Families can be filtered by the name of the father, mother, or a child, sources by author, and places and repositories by their type.
- **Advanced filter** – a condition builder for filters the ready-made ones can't express, described [below](#advanced-filter).
- **GOQL** – a text field for an expression in the [Gramps Object Query Language](goql.md), with syntax highlighting. Type the expression and press Enter or click **Apply**. If the expression is invalid, the field is marked as an error. An expression applies on top of the other filters.

Active filters are shown as chips in a row below the toolbar. Remove a single filter by clicking the chip's clear button, or use **Clear all filters** to remove them all at once.

### Advanced filter

Click **Advanced filter** at the bottom of the filter panel to open the condition builder. Its conditions are the filter rules known from Gramps Desktop, such as "People with the &lt;name&gt;" or "Ancestors of &lt;person&gt;".

- Click **Add condition** to pick a rule. The rules are grouped into categories and can be searched by name or description.
- Fill in the rule's parameters. Each parameter has a matching input, for example a date field, a tag selector, or an object selector for a person or place.
- Choose how the conditions of a group are combined: **All conditions**, **Any condition**, or – via the menu next to them – **Exactly one condition**.
- Click **Add group** to add a group of conditions inside another group, with its own way of combining them.
- Select **Not** on a condition or group to invert it.

Click **Apply** to filter the list.

The ready-made filters and the GOQL expression that are active when you open the builder appear there as conditions. A GOQL expression can also be added as a condition of its own, for example to combine several expressions with **Any condition**. If the filter you build can be expressed with the ready-made filters, it is shown with them after applying. Otherwise, it is shown as a single **Advanced filter** chip, and the filter panel offers an **Edit** button to reopen the builder.

!!! note
    Rules that refer to custom filters saved in Gramps Desktop are not available in the builder. The rules are shown in your language with Gramps Web API 3.24 or newer.

## Selecting objects and acting on them in bulk

Users with edit permissions see a **Select** button next to the filter button. Click it to enter selection mode, which adds a checkbox to every row.

Tick the objects you want, and a toolbar appears showing how many are selected, along with an **Action** dropdown and an **Apply** button.

The checkbox in the table header selects all objects on the current page. If more objects match the current filters, the toolbar then offers **Select All (N)**, which selects all N matching objects across all pages. Unticking a row, changing the page or the filters, or leaving selection mode ends this selection.

### Delete

Select one or more objects, choose **Delete**, and click **Apply**. A confirmation dialog asks you to confirm, warning that the action cannot be undone.

Deleting more than ten objects runs as a background task. Its progress is shown next to the **Apply** button and in [Notifications](notifications.md), and the list reloads when it is done.

!!! tip
    Deletions are recorded in the [revision history](revisions.md) like any other change, so a mistaken bulk delete can be reversed by undoing the corresponding transaction.

### Merge

Select **exactly two** objects, choose **Merge**, and click **Apply**. A dialog asks which of the two should provide the primary data for the merged object; click the one you want to keep as primary. The other object's data is merged into it and references are updated.

Merging is available for people, families, events, places, sources, and citations. It is not available for repositories, notes, and media objects.

In the media view, selection works in both the gallery and the list layout: in selection mode, clicking a tile or row toggles it. **Delete** is the only action available for media.

If you choose an action without a valid selection – for example a merge with only one object selected – a dialog explains what is required.
