# Customize the tree

Tree owners and administrators can adapt the name and look of the tree, as well as its home page, for all users. These settings are found in the **Tree settings** and **Customization** sections of the [Administration settings](settings.md).

## Family Tree name

!!! note
    Renaming the tree only works in a [multi-tree setup](../install_setup/multi-tree.md) or when `TREE_ID` is explicitly set in the [server configuration](../install_setup/configuration.md). On a default single-tree installation without `TREE_ID` set, this will raise an error.

This allows changing the name of the underlying Gramps family tree database. Enter a new name and click **Rename** to apply.

!!! tip
    If you only want to change the name shown in the app bar without renaming the database, use the [App title](#app-title) setting instead.

## Researcher Information

Set the name, address, and contact details of the primary researcher. This information is embedded in exports (e.g. GEDCOM files).

## Theme colors

Set a custom **primary color** and **accent color** for the Gramps Web interface. These colors are applied to all users of this tree and take effect immediately after saving.

Use the color pickers to select colors, then click **Save**. Click **Reset** to revert to the defaults.

## App title

Set a custom title for the application. If set, this overrides the family tree name in the browser title bar and the top app bar.

Enter a title and click **Save**. Leave blank to use the default (the family tree name).

## Home page note

Select a Gramps **Note** object to display on the dashboard home page. The note content is rendered below the main dashboard columns and is visible to all users with access to the tree.

Use the object selector to search for and pick a note, then save. Click **Remove** to clear the current home page note.

## Home page image

Select a Gramps **Media** object to display as an image on the dashboard home page. When combined with a home page note, the image appears beside the note text. Without a note, only the image is shown.

Use the object selector to search for and pick a media object, then save. Click **Remove** to clear the current home page image.

## Export/Import settings

Tree-level settings (app title, theme colors, home page note/image, etc.) can be exported as a JSON file for backup or to copy to another Gramps Web instance.

- Click **Export settings** to download the current settings as a JSON file.
- Click **Import tree settings** to upload a previously exported JSON file and apply the settings.
