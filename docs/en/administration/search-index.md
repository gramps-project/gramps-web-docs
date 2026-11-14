# Search index

The **Search index** section of the [Administration settings](settings.md) shows the state of the full-text search index and lets you rebuild it.

## Manage search index

Gramps Web maintains a full-text search index that is normally updated automatically whenever data changes. The status indicator shows how many objects are currently indexed versus the total object count.

Click **Update search index** to trigger a full rebuild. A progress indicator is shown while the task runs in the background. This is rarely needed.

If a tree has no search index yet, for example after a server upgrade that changed the index format, Gramps Web builds it in the background the first time the tree is opened. While it is being built, the section shows "The search index is being built." instead of the counts, **Update search index** is disabled, and search results may be incomplete. The build shows up in [Notifications](../user-guide/notifications.md) as the "Update search index" task.
