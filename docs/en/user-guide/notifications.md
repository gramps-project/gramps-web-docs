# Notifications

**Notifications** is a sidebar item with a bell icon. When errors have occurred or background tasks are running, a badge shows the number of unread notifications. Click it to open the notification log.

The notification log serves two purposes:

- It is a record of errors that occurred during your session – failed API requests, background task errors, save failures, or browser-level errors.
- It tracks the progress of long-running background tasks – such as imports and exports, generating reports, OCR text recognition, database upgrades, and search/semantic index rebuilds – showing their state (e.g. pending, started, in progress) and notifying you when they complete or fail.

Each entry shows a short message, the source (Network, Task, Save, or Browser), and a timestamp.

Some notifications include structured detail. Clicking such an entry opens a dialog with a breakdown of the error data and a **Copy JSON** button. This is useful when reporting a bug, as the JSON contains the exact error information from the server.

Use **Clear All** to dismiss all notifications.

!!! note
    Notifications are stored in memory only and are cleared when you reload the page.
