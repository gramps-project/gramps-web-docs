# Administration Settings

The **Settings > Administration** page is accessible via the user icon in the top app bar. It is only available to users with the Owner or Administrator role and provides tools for managing the family tree database.

The page is organized into collapsible sections. Click a section header to expand it.

## Data

Covers usage quotas, importing data, and media file management.

### Usage quotas

The top of the section shows current usage relative to any configured limits:

- **People** – the number of person objects in the tree versus the configured maximum (∞ if unlimited)
- **Media storage** – total size of uploaded media files versus the configured storage quota (∞ if unlimited)

Quotas are set by the server administrator; see [Server configuration](../install_setup/configuration.md) for details.

### Import data

The import section lets you upload a family tree file or a media archive. See [Import data](import.md) for full instructions.

### Media file status

This section shows:

- The total number of media objects in the tree and whether any are missing a checksum
- The number of media objects whose associated file is missing from the server

A green check mark indicates everything is in order. If problems are detected, links to the affected objects are shown. Missing checksums typically occur when data was imported from a format such as GEDCOM that includes media references but not the actual files. The missing files can be uploaded via the import media archive feature.

### Import media archive

Allows uploading a ZIP file of media files to fill in missing files. See [Import data](import.md) for full instructions.

## Search index

### Manage search index

Gramps Web maintains a full-text search index that is normally updated automatically whenever data changes. The status indicator shows how many objects are currently indexed versus the total object count.

Click **Update search index** to trigger a full rebuild. A progress indicator is shown while the task runs in the background. This is usually only needed after a server upgrade.

### Semantic search index

!!! warning "Deprecated"
    Semantic search is deprecated and will be removed in Gramps Web API 3.25, together with this section. AI chat does not need it since Gramps Web API 3.24.

If the server has [semantic (AI-powered) search enabled](../install_setup/chat.md#semantic-search-deprecated), an additional section appears with two actions:

- **Regenerate semantic search index** – rebuilds the entire semantic index from scratch. This is computationally expensive and can take a long time.
- **Update semantic search index** – performs an incremental update, adding only objects not yet indexed. Faster than a full rebuild.

## Tree settings

### Family Tree name

!!! note
    Renaming the tree only works in a [multi-tree setup](../install_setup/multi-tree.md) or when `TREE_ID` is explicitly set in the [server configuration](../install_setup/configuration.md). On a default single-tree installation without `TREE_ID` set, this will raise an error.

This allows changing the name of the underlying Gramps family tree database. Enter a new name and click **Rename** to apply.

!!! tip
    If you only want to change the name shown in the app bar without renaming the database, use the [App title](#app-title) setting instead.

### Researcher Information

Set the name, address, and contact details of the primary researcher. This information is embedded in exports (e.g. GEDCOM files).

## Customization

### Theme colors

Set a custom **primary color** and **accent color** for the Gramps Web interface. These colors are applied to all users of this tree and take effect immediately after saving.

Use the color pickers to select colors, then click **Save**. Click **Reset** to revert to the defaults.

### App title

Set a custom title for the application. If set, this overrides the family tree name in the browser title bar and the top app bar.

Enter a title and click **Save**. Leave blank to use the default (the family tree name).

### Home page note

Select a Gramps **Note** object to display on the dashboard home page. The note content is rendered below the main dashboard columns and is visible to all users with access to the tree.

Use the object selector to search for and pick a note, then save. Click **Remove** to clear the current home page note.

### Home page image

Select a Gramps **Media** object to display as an image on the dashboard home page. When combined with a home page note, the image appears beside the note text. Without a note, only the image is shown.

Use the object selector to search for and pick a media object, then save. Click **Remove** to clear the current home page image.

### Export/Import settings

Tree-level settings (app title, theme colors, home page note/image, etc.) can be exported as a JSON file for backup or to copy to another Gramps Web instance.

- Click **Export settings** to download the current settings as a JSON file.
- Click **Import tree settings** to upload a previously exported JSON file and apply the settings.

## Family Tree Processing

### Check and Repair Database

This tool checks the Gramps database for internal inconsistencies and fixes the ones it can – analogous to the [Check and Repair Database tool](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) in Gramps Desktop.

Click **Check and Repair** and wait for the progress indicator to complete. The result is shown below the button:

- If no errors were found, a confirmation message is displayed.
- If errors were found, a summary of the fixes applied is shown.

Run this tool if you encounter unexpected errors or behavior that may be caused by database inconsistencies, such as missing relationships between objects.

### Verify the Data

While [Check and Repair Database](#check-and-repair-database) looks for *technical* inconsistencies, this tool looks for *implausible* data – analogous to the [Verify the Data tool](https://gramps-project.org/wiki/index.php/Gramps_5.0_Wiki_Manual_-_Tools#Verify_the_Data) in Gramps Desktop. It reports things that are not impossible but are unlikely enough to be worth a second look, such as a mother aged 12 or a person who lived to 130.

Under **Options** you can adjust the thresholds the tests use – maximum age, minimum and maximum age to marry or to have children, maximum number of children, and so on – as well as whether to estimate missing or inexact dates and whether to report invalid dates such as 31 February.

Click **Verify the Data** to start. The check runs as a background task, and the findings are then listed under **Data Verification Results**. Nothing is changed by this tool: it only reports what it finds.

!!! note
    A finding is not proof of an error. Long lives and large age gaps do occur, so treat the results as a list of things to check rather than a list of things to fix.

## Tags

### Manage tags

Create, rename, recolor, and delete [tags](../user-guide/tags.md) for the family tree. Tags are stored in the Gramps database, shared across all users, and fully compatible with Gramps Desktop.

Click **New Tag** to create a tag. Use the controls next to an existing tag to rename it (pencil icon), change its colour (colour picker), or delete it (delete icon).

!!! note
    Deleting a tag removes it from all objects it was applied to.

See [Tags](../user-guide/tags.md) for how tags are used throughout Gramps Web, including the special `Blog` and `ToDo` tags.

## Backups

A backup contains the family tree data, including private records, the tree settings, and the users of the tree. Media files are not included; see [Back up your media files](export.md#back-up-your-media-files).

### Stored backups

If the server administrator has set a backup directory (`BACKUP_DIR`, see [Server configuration](../install_setup/configuration.md)), backups can be stored on the server. Otherwise, the section shows a notice that storing backups is not configured, and only restoring from an uploaded file is available.

Click **Make Backup...** to create a backup. It is created as a background task and then appears in the list of stored backups, with its date, the number of people, and its size. The server keeps only the newest backups (five by default) and deletes older ones automatically. The number of backups that can be created per day is limited as well.

For each stored backup, you can:

- **Download** it as a `.tar` file, for example to keep a copy elsewhere.
- **Restore** it, as described below.
- **Delete** it, after confirming.

A backup made with a newer version of Gramps Web than the one running on the server is marked with a warning icon and cannot be restored.

### Restore from Backup

Restores the tree from a stored backup or from an uploaded file. To restore a stored backup, click the restore button next to it. To restore from a file, select a Gramps Web backup (`.tar`) or a Gramps XML file (`.gramps`) and click **Restore**.

!!! danger
    Restoring the data is a destructive replace, not a merge. Any existing object not present in the backup is deleted.

For a Gramps Web backup, a dialog shows when the backup was made, for which tree, and with which version, and lets you choose which parts to restore:

- **Data** – the objects of the family tree
- **Tree settings** – the settings of this page, such as theme colors, app title, and home page note
- **Users** – the users of the tree

Click **Preview** to see what the restore would change. A Gramps XML file only contains data, so for such a file the preview starts right away. You will be asked to re-authenticate if your session isn't fresh enough. The preview runs as a background task and, once complete, opens a dialog summarizing the changes per object type (people, families, events, places, citations, sources, repositories, media objects, notes, tags), and for the tree settings and users if selected:

- **Add** – objects present in the backup but missing from the current tree
- **Update** – objects present in both that differ
- **Delete** – objects in the current tree that are absent from the backup
- **Unchanged** – objects identical in both

If any objects would be deleted, the dialog warns how many. Review the summary, then click **Restore** to apply the changes, or **Cancel** to abort.

After the restore, users that were added from the backup are listed. They get a random password, so they have to reset their password before they can sign in. Users that already exist on the server are never changed. Media objects whose files are missing on the server are listed as well; upload them via [Import media archive](#import-media-archive).

!!! note
    Restoring data only restores object data and media references. Binary media files themselves and tree metadata (default person, bookmarks, name groups) are not affected.

!!! tip
    Use this to roll back a tree to a known-good backup, for example after a bad import or an unwanted bulk edit.

## Danger Zone

!!! danger
    Actions in the Danger Zone are **irreversible**. Make a [backup](#backups) before proceeding.

### Delete all objects

Removes objects from the family tree. Clicking **Delete** opens a dialog where you can choose to delete:

- **All objects** – completely clears the tree
- **Specific object types** – for example, only events or only media objects

You will be asked to re-authenticate (log in again) to confirm the action. The deletion runs as a background task and a progress indicator is shown.

!!! warning
    Deleting only a subset of object types (rather than all objects at once) can take a very long time for large trees, as the server must check and update all relationships between objects.

!!! tip
    Use this to start fresh before importing a new tree, or to remove specific object types that were imported incorrectly.
