# Tags

Tags are labels that can be applied to any object in the Gramps database – people, families, events, places, sources, citations, repositories, notes, and media. They are useful for grouping and filtering objects. Tags are stored in the Gramps family tree database and are shared across all users; they are also fully compatible with tags created in Gramps Desktop.


## Managing tags

Tags are managed from the **Tags** section of [Administration Settings](../administration/settings.md#tags), which is only available to users with the Owner or Administrator role. It shows all existing tags and allows you to:

- **Create** a new tag using the **New Tag** button
- **Rename** a tag using the edit (pencil) icon
- **Change the colour** of a tag using the colour picker
- **Delete** a tag using the delete icon

!!! note
    Deleting a tag removes it from all objects it was applied to.

## Applying tags to objects

Tags can be applied to or removed from an object on its detail page when in edit mode.

## Filtering by tag

All object list pages (People, Families, Events, Places, Sources, Citations, Repositories, Notes, Media) include a tag filter. Use it to show only objects that have a specific tag applied.

## Special tags

Two tags have a special meaning in Gramps Web:

- **`Blog`** – any source tagged `Blog` is treated as a blog post and appears in the [Blog](blog.md) view
- **`ToDo`** – any note tagged `ToDo` is treated as a research task and appears in the [Tasks](tasks.md) view

These tags are created automatically when you first use the Blog or Tasks features. Renaming or deleting them will break the corresponding feature.
