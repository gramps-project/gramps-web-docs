# Import data

You can bring an existing family tree into Gramps Web by uploading a file exported from another genealogy program, from an online service, or from Gramps Desktop.

The import is found in the **Data** section of the [Administration settings](settings.md) (user icon in the top app bar ▸ Administration), which is available to tree owners and administrators. While the tree is still empty, the **Import Family Tree** button on the home page's "Get started" card leads there as well.

## Which file to use

| Coming from | Export your tree as | File extension |
|---|---|---|
| Another genealogy program or online service | GEDCOM | `.ged` |
| Gramps Desktop | Gramps XML | `.gramps` |
| GeneWeb | GeneWeb | `.gw` |
| Pro-Gen | Pro-Gen | `.def` |
| A spreadsheet | Gramps CSV | `.csv` |
| An address book | vCard | `.vcf` |

GEDCOM is the common exchange format that almost every genealogy program and online service can export. Look for an "Export" or "Download" option in your program or on the website, and choose GEDCOM if you are offered several formats. The Gramps Wiki page [Import from another genealogy program](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) has notes on specific programs.

If you use Gramps Desktop, choose Gramps XML (`.gramps`) rather than GEDCOM. It carries all Gramps data without loss, and your online and offline trees keep the same identifiers, so they can be [synchronized](sync.md). See [Coming from Gramps Desktop](#coming-from-gramps-desktop) below.

## Import a family tree file

1. Open the **Data** section of the Administration settings.
2. Under "Import Family Tree", choose your file and click **Import**.
3. The file is parsed first, and a "Confirm Import" dialog shows how many objects it contains (people, families, events, places, and so on). Nothing has been added to your tree yet. Check that the counts look plausible, then click **Import** to proceed, or **Cancel** to abort without changing anything.
4. The import runs in the background and a progress indicator is shown. Once the data is imported, the search index is updated, which can take a while for a large tree.

When the import has finished, check the result: compare the number of people in the **Statistics** panel on the home page with the number in your old program, and open a family you know well to see that parents, children, dates, and places came across as expected.

!!! warning
    A regular import is purely additive: it always creates new objects and never updates or deletes existing ones, even for objects that already exist in your tree under the same Gramps ID or handle. Importing the same file twice – or importing a file that overlaps with data already in the tree – will duplicate every matching object rather than merge or skip it.

    If you need to bring in changes made elsewhere to a tree that was already imported, use [Restore from Backup](settings.md#restore-from-backup) instead, which replaces the tree to match the uploaded file rather than adding to it. This requires a Gramps XML file.

If a limit on the number of people has been set for your tree (see [Usage quotas](settings.md#usage-quotas)), an import that would exceed it is refused as a whole.

## GEDCOM files

Both GEDCOM 5.5.1 and GEDCOM 7 files can be imported. There are a few things to be aware of.

### Character encoding

A GEDCOM 5.5.1 file declares its character encoding in its header. UTF-8, UTF-16, ANSEL, and Windows (ANSI) encodings are supported. If names with accents or other special characters look garbled after the import (for example `MÃ¼ller` instead of `Müller`), the file was probably exported with a different encoding than the one it declares. Export the file again from your old program, choosing UTF-8 if it offers a choice, and [start over](#starting-over).

GEDCOM 7 files must always be encoded as UTF-8; other files are rejected with an "Invalid GEDCOM file" error.

### Program-specific data

Many programs add their own extensions to GEDCOM that other programs don't understand. Gramps does not silently drop such data: lines it cannot interpret are collected in a note of the type "GEDCOM import", attached to the person, family, or other object they belong to. Review these notes to see whether anything important didn't come across.

### Media files

A GEDCOM file contains references to media files (such as photos or scanned documents), but not the files themselves. After the import, the media objects exist in your tree, but their files are missing, which is shown under [Media file status](settings.md#media-file-status). To add the files, see [Import media files](#import-media-files) below.

## Coming from Gramps Desktop

If you are using Gramps Desktop, there are two steps to prepare your database to make sure everything will run smoothly in the following.

1. Check and repair the database
    - Optional: create a database backup by exporting to Gramps XML
    - Run the [Check and repair database tool](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database). This fixes some internal inconsistencies that could lead to problems in Gramps Web.
2. Convert media paths to relative
    - Use the Gramps Media Manager to [convert all media paths from absolute to relative](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute). Note that even with relative paths, any media files outside of your Gramps media directory will not work properly when synchronized with Gramps Web.

Then export your tree to Gramps XML (`.gramps`), import it as described above, and upload your media files as described in the next section. To keep working on the same tree on your computer and on the web, use the [Gramps Web Sync addon](sync.md).

### Why no support for Gramps XML package?

While Gramps XML (`.gramps`) is the preferred format for importing data, Gramps XML *package* (`.gpkg`) is not supported by Gramps Web. This is because the import and export routines for media files are not suited for use on a web server.

## Import media files

If you have imported a family tree and need to upload the corresponding media files, use **Import Media Files** in the Data section of the Administration settings. It expects a ZIP file containing the missing media files. Files are matched to media objects in your tree in one of two ways:

- **By checksum.** For media objects that have a checksum – as is the case for trees imported from Gramps Desktop – the file with the matching checksum is used, regardless of its name or the folder structure in the ZIP file. This only works if the checksums in the Gramps database are correct, which running the check and repair tool ensures.
- **By path.** Media objects without a checksum – as is typical after a GEDCOM import – are matched by their path: the ZIP file must contain the file under exactly the relative path stored in the media object.

If the paths stored in your GEDCOM file are absolute (for example `C:\Users\...\photo.jpg`), matching by path will not work. In this case, it is recommended to first import everything into Gramps Desktop, which has more options to associate existing media files with an imported tree, and then move to Gramps Web as described in [Coming from Gramps Desktop](#coming-from-gramps-desktop).

## Common problems

**"Unsupported format".** Only the file extensions listed [above](#which-file-to-use) can be imported. If your program or online service gave you a ZIP archive, unpack it and upload the `.ged` file inside.

**Everything appears twice.** The same file was imported twice. Since imports never merge, [start over](#starting-over).

**Garbled special characters.** See [Character encoding](#character-encoding).

**Photos are missing.** See [Import media files](#import-media-files).

### Starting over

If an import went wrong, or you want to fix something in your old program and import again, first empty the tree using [Delete all objects](settings.md#delete-all-objects) in the Danger Zone of the Administration settings, then import the corrected file. Note that this also deletes any changes you have made in Gramps Web since the import.
