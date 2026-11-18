# Import media files

If you have [imported a family tree](import.md) and need to upload the corresponding media files, use **Import Media Files** on the [Import page](import.md), below the family tree import. It expects a ZIP file containing the missing media files. The upload is only possible once the tree contains media objects, since the files are matched to existing media objects – a family tree file only refers to its media files, so import it first.

Files are matched to media objects in your tree in one of two ways:

- **By checksum.** For media objects that have a checksum – as is the case for trees imported from Gramps Desktop – the file with the matching checksum is used, regardless of its name or the folder structure in the ZIP file. This only works if the checksums in the Gramps database are correct, which running the check and repair tool ensures.
- **By path or file name.** Media objects without a checksum – as is typical after a GEDCOM import – are matched by the relative path stored in the media object. If no file in the ZIP has that path, they are matched by file name alone, ignoring upper and lower case (since Gramps Web API 3.26). This also works for absolute paths from other programs, such as `C:\Users\...\Family\grandpa.jpg`, so you can simply put all files into the ZIP file. A file name is only used if it is unique, both in the ZIP file and among the media objects still without a file.

After the upload, the result says for how many media objects a file was found, and lists those for which the ZIP file had no file, with their Gramps ID and stored path. Use this list to find the missing files, then upload another ZIP file with just these – files that are already on the server are not affected.

If several media objects have the same file name in different folders, matching by file name doesn't work for them. Either recreate the folder structure from the stored paths in the ZIP file, or import everything into Gramps Desktop first, which has more options to associate existing media files with an imported tree, and then move to Gramps Web as described in [Coming from Gramps Desktop](import.md#coming-from-gramps-desktop).

## Media file status

The **Data** section of the [Administration settings](settings.md) shows:

- The total number of media objects in the tree and whether any are missing a checksum
- The number of media objects whose associated file is missing from the server

A green check mark indicates everything is in order. If problems are detected, links to the affected objects are shown. Missing checksums typically occur when data was imported from a format such as GEDCOM that includes media references but not the actual files. The missing files can be uploaded as described above.
