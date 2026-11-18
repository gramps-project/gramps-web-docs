# Notifications

The bell in the top app bar opens the notifications. A badge on the bell shows the number of unread notifications. The menu lists running tasks and the latest notifications; **Show all** opens the full notification log. On small screens, the bell opens the log directly.

Notifications are about:

- **Changes by other users.** When other users change the tree while you are using Gramps Web, a notification says who changed what, e.g. "Edit Person" or "12 changes". Click it to open the change in the [revision history](revisions.md). Changes that have no Gramps Web user, such as changes made directly to a shared database with Gramps Desktop, are shown without a name. This is only available to users who can see the revision history (members and above).
- **Background tasks** – such as imports and exports, generating reports, OCR text recognition, database upgrades, deleting or editing many objects, and search index rebuilds – showing their state (e.g. pending, started, in progress) and notifying you when they complete or fail.
- **Errors** that occurred during your session – failed API requests, background task errors, save failures, or browser-level errors.

Finished exports and media archives can be downloaded from their notification, also after you have left the [Export page](../administration/export.md).

Some notifications include structured detail, such as the error message of a failed task. Clicking such an entry in the notification log opens a dialog with a breakdown of the error data and a **Copy JSON** button. This is useful when reporting a bug, as the JSON contains the exact error information from the server.

Use **Clear All** in the notification log to dismiss all notifications.

Tasks that change the whole tree, such as an import, a restore, deleting all objects, or rebuilding the search index, cannot run at the same time. If you start one while another is running, a message says that another task is already running on this tree, and the running task is shown with its progress.

!!! note
    Notifications are stored in memory only and are cleared when you reload the page. Gramps Web checks for changes by other users only while it is open, so changes made while you were away are not reported; see [Revision history](revisions.md) for those.
