

## Prepare your Gramps database

If you are using Gramps Desktop, there are two steps to prepare your database to make sure everything will run smoothly in the following. If you are migrating from a different genealogy program, you can skip this step.

1. Check and repair the database
    - Optional: create a database backup by exporting to Gramps XML
    - Run the [Check and repair database tool](https://gramps-project.org/wiki/index.php/Gramps_5.1_Wiki_Manual_-_Tools#Check_and_Repair_Database). This fixes some internal inconsistencies that could lead to problems in Gramps Web.
2. Convert media paths to relative
    - Use the Gramps Media Manager to [convert all media paths from absolute to relative](https://gramps-project.org/wiki/index.php/Gramps_5.1_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute). Note that even with relative paths, any media files outside of your Gramps media directory will not work properly when synchronized with Gramps Web.

## Import genealogical data

To import an existing family tree, use the "Import" page and upload a file in any of the file formats supported by Gramps &ndash; see [Import from another genealogy program](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) in the Gramps Wiki.

If you already use Gramps Desktop, it is strongly recommended to use the Gramps XML (`.gramps`) format to ensure your online and offline trees use the same identifiers and can be [synchronized](sync.md).

## Why no support for Gramps XML package?

While Gramps XML (`.gramps`) is the preferred format for importing data, Gramps XML *package* (`.gpkg`) is not supported by Gramps Web. This is because the import and export routines for media files are not suited for use on a web server.

To import the media files belonging to an imported `.gramps` file, see the next section.

## Import media files

If you have uploaded a family tree and need to upload the corresponding media files, you can use the "import media archive" button on the "Import" page.

It expects a ZIP file with the missing media files inside. The folder structure in the ZIP file does not have to be the same as the folder structure inside the Gramps media folder as the files are matched to media objects by their checksum.

Note that this feature only works for files that have the correct checksum in the Gramps database (which should be ensured by running the check and repair tool in the first step).

When moving to Gramps Web from a different genalogy program including media files, it is recommended to first import everything into Gramps Desktop, which has more options to associate existing media files with an imported tree.