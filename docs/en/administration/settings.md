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

If the server has [semantic (AI-powered) search enabled](../install_setup/configuration.md), an additional section appears with two actions:

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

## Danger Zone

!!! danger
    Actions in the Danger Zone are **irreversible**. Make a backup before proceeding.

### Delete all objects

Removes objects from the family tree. Clicking **Delete** opens a dialog where you can choose to delete:

- **All objects** – completely clears the tree
- **Specific object types** – for example, only events or only media objects

You will be asked to re-authenticate (log in again) to confirm the action. The deletion runs as a background task and a progress indicator is shown.

!!! warning
    Deleting only a subset of object types (rather than all objects at once) can take a very long time for large trees, as the server must check and update all relationships between objects.

!!! tip
    Use this to start fresh before importing a new tree, or to remove specific object types that were imported incorrectly.
