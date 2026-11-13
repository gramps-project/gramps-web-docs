# Import media files

If you have [imported a family tree](import.md) and need to upload the corresponding media files, use **Import Media Files** in the Data section of the [Administration settings](settings.md). It expects a ZIP file containing the missing media files. Files are matched to media objects in your tree in one of two ways:

- **By checksum.** For media objects that have a checksum – as is the case for trees imported from Gramps Desktop – the file with the matching checksum is used, regardless of its name or the folder structure in the ZIP file. This only works if the checksums in the Gramps database are correct, which running the check and repair tool ensures.
- **By path.** Media objects without a checksum – as is typical after a GEDCOM import – are matched by their path: the ZIP file must contain the file under exactly the relative path stored in the media object.

If the paths stored in your GEDCOM file are absolute (for example `C:\Users\...\photo.jpg`), matching by path will not work. In this case, it is recommended to first import everything into Gramps Desktop, which has more options to associate existing media files with an imported tree, and then move to Gramps Web as described in [Coming from Gramps Desktop](import.md#coming-from-gramps-desktop).
