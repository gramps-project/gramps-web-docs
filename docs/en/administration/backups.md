# Back up and restore

Tree owners can create, download, and restore backups of the tree in the **Backups** section of the [Administration settings](settings.md).

A backup contains the family tree data, including private records, the tree settings, and the users of the tree. Media files are not included; see [Back up your media files](export.md#back-up-your-media-files).

## Stored backups

If the server administrator has set a backup directory (`BACKUP_DIR`, see [Server configuration](../install_setup/configuration.md)), backups can be stored on the server. Otherwise, the section shows a notice that storing backups is not configured, and only restoring from an uploaded file is available.

Click **Make Backup...** to create a backup. It is created as a background task and then appears in the list of stored backups, with its date, the number of people, and its size. The server keeps only the newest backups (five by default) and deletes older ones automatically. The number of backups that can be created per day is limited as well.

For each stored backup, you can:

- **Download** it as a `.tar` file, for example to keep a copy elsewhere.
- **Restore** it, as described below.
- **Delete** it, after confirming.

A backup made with a newer version of Gramps Web than the one running on the server is marked with a warning icon and cannot be restored.

## Restore from Backup

Restores the tree from a stored backup or from an uploaded file. To restore a stored backup, click the restore button next to it. To restore from a file, select a Gramps Web backup (`.tar`) or a Gramps XML file (`.gramps`) and click **Restore**.

!!! danger
    Restoring the data is a destructive replace, not a merge. Any existing object not present in the backup is deleted.

For a Gramps Web backup, a dialog shows when the backup was made, for which tree, and with which version, and lets you choose which parts to restore:

- **Data** – the objects of the family tree
- **Tree settings** – the settings of the Administration page, such as theme colors, app title, and home page note
- **Users** – the users of the tree

Click **Preview** to see what the restore would change. A Gramps XML file only contains data, so for such a file the preview starts right away. You will be asked to re-authenticate if your session isn't fresh enough. The preview runs as a background task and, once complete, opens a dialog summarizing the changes per object type (people, families, events, places, citations, sources, repositories, media objects, notes, tags), and for the tree settings and users if selected:

- **Add** – objects present in the backup but missing from the current tree
- **Update** – objects present in both that differ
- **Delete** – objects in the current tree that are absent from the backup
- **Unchanged** – objects identical in both

If any objects would be deleted, the dialog warns how many. Review the summary, then click **Restore** to apply the changes, or **Cancel** to abort.

After the restore, users that were added from the backup are listed. They get a random password, so they have to reset their password before they can sign in. Users that already exist on the server are never changed. Media objects whose files are missing on the server are listed as well; upload them via [Import media files](import-media.md).

!!! note
    Restoring data only restores object data and media references. Binary media files themselves and tree metadata (default person, bookmarks, name groups) are not affected.

!!! tip
    Use this to roll back a tree to a known-good backup, for example after a bad import or an unwanted bulk edit.

## Gramps XML as a backup

If storing backups is not available, or you only want to keep a copy of the family tree data, [export](export.md) the tree as Gramps XML. Such a file can be restored via [Restore from Backup](#restore-from-backup) as well.

Note that if your Gramps Web user does not have permission to view private records, the export will not be a full backup, since it will not contain any private records.
