# Administration Settings

The **Settings > Administration** page is accessible via the user icon in the top app bar. It is only available to users with the Owner or Administrator role and provides tools for managing the family tree database.

## Usage quotas

The top of the page shows current usage relative to any configured limits:

- **People** – the number of person objects in the tree versus the configured maximum (∞ if unlimited)
- **Media storage** – total size of uploaded media files versus the configured storage quota (∞ if unlimited)

Quotas are set by the server administrator; see [Server configuration](../install_setup/configuration.md) for details.

## Import data

The import section lets you upload a family tree file or a media archive. See [Import data](import.md) for full instructions.

## Media file status

This section shows:

- The total number of media objects in the tree and whether any are missing a checksum
- The number of media objects whose associated file is missing from the server

A green check mark indicates everything is in order. If problems are detected, links to the affected objects are shown. Missing checksums typically occur when data was imported from a format such as GEDCOM that includes media references but not the actual files. The missing files can be uploaded via the import media archive feature.

## Import media archive

Allows uploading a ZIP file of media files to fill in missing files. See [Import data](import.md) for full instructions.

## Manage search index

Gramps Web maintains a full-text search index that is normally updated automatically whenever data changes. The status indicator shows how many objects are currently indexed versus the total object count.

Click **Update search index** to trigger a full rebuild. A progress indicator is shown while the task runs in the background. This is usually only needed after a server upgrade.

### Semantic search index

If the server has [semantic (AI-powered) search enabled](../install_setup/configuration.md), an additional section appears with two actions:

- **Regenerate semantic search index** – rebuilds the entire semantic index from scratch. This is computationally expensive and can take a long time.
- **Update semantic search index** – performs an incremental update, adding only objects not yet indexed. Faster than a full rebuild.

## Family Tree name

!!! note
    Renaming the tree only works in a [multi-tree setup](../install_setup/multi-tree.md) or when `TREE_ID` is explicitly set in the [server configuration](../install_setup/configuration.md). On a default single-tree installation without `TREE_ID` set, this will raise an error.

This allows to change the name of the underlying Gramps family tree database. Enter a new name and click **Rename** to apply.

## Check and Repair Database

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
