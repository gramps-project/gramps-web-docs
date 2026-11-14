# Export data

The Export page lets you download the family tree data in various formats, as well as an archive of all media files.

## Export the family tree as Gramps XML

To get a copy of the family tree data, open the Export page in Gramps Web and select the Gramps XML format. Clicking on "export" will generate the file and start the download once it is ready.

Note that if your Gramps Web user does not have permission to view private records, the export will not contain any private records.

## Back up your family tree

For complete backups of the tree – including its settings and users – see [Back up and restore](backups.md). A Gramps XML export can serve as a backup of the family tree data only and can be restored via [Restore from Backup](backups.md#restore-from-backup).

## Share your family tree with users of other genealogy programs

When sharing genealogical data as Gramps XML is not an option, you can also export a GEDCOM file. Note that this is not suited as a backup of your Gramps Web tree.

## Back up your media files

To back up your media files, you can create and download a ZIP archive of all media files on the Export page.

Note that, especially for large trees, this can be an expensive operation for the server and should only be done if absolutely necessary. For this reason, the number of media archives that can be created is limited (by default to one per hour). If you reach the limit, the error message shows it.

A better option to back up your media files on a regular basis is to use the [Gramps Web Sync addon](sync.md) (which itself is not a backup solution) and create incremental backups on your local computer.

In both bases, if your Gramps Web user does not have permission to view private records, the export will not contain files of private media objects.

## Move to a different Gramps Web instance

Gramps Web does not lock you in with a specific provider and you can always move to a different Gramps Web instance without loosing any data, and without having direct access to either of the servers.

To achieve a full migration, follow these steps (assuming you have tree owner permissions):

1. Go to the Export page and export your tree as a Gramps XML (`.gramps`) file. If you use the [Sync addon](sync.md), you can also generate the export in Gramps desktop.
2. On the Export page, generate & download a media archive. If you use the [Sync addon](sync.md), you can also simply ZIP your local Gramps media folder.
3. Go to Settings > Administration > Manage users and click the "Export user details" button. It will download a JSON file.
4. In the new Gramps Web instance, open the Import page. Import the `.gramps` file exported in step 1.
5. On the Import page of the new Gramps Web instance, upload the media archive (ZIP).
6. Go to Settings > Administration > Manage users of the new Gramps Web instance. Click the "Import user accounts" button and upload the JSON file downloaded in step 3.

Note that, while your user accounts will be migrated, all your users will need to set new passwords by using the "forgot password" link, since passwords are stored in encrypted form and cannot be exported.