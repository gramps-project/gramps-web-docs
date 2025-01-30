# Working with DNA matches

DNA matches are segments of DNA that agree between to individuals, identified by the presence of markers, so-called SNPs (the acronym for single nucleotide polymorphisms, pronounced &ldquo;snips&rdquo;).

To obtain this data, you need access to a DNA test that is uploaded to a matching database that allows to view DNA segment match data (e.g. MyHeritage, Gedmatch, FamilytreeDNA). Gramps Web does not perform the matching itself, as it only has access to the data you upload.

## Entering DNA match data

To enter DNA match data, you need [edit permissions](../install_setup/users.md) as the data is stored as a note in the Gramps database. The DNA view, accessible from the main menu, provides a convenient way to enter this data in the right format.

To enter a new match, click on the + button in the lower right. In the dialog that opens, select the two individuals. Note that the &ldquo;First person&rdquo; and the &ldquo;Second person&rdquo; are treated differently: the match is stored as an association from the first to the second person. Only the first person will be selectable for the DNA match view and chromosome browser. Typically, the first person is the one whose DNA test you have access to and the second person is a more distant relative.

If the second person is not in the database, you need to create it first by using the &ldquo;Create person&rdquo; button in the top right corner of the user interface. Once you have created the person, you can return to the DNA match view and select the newly created person.

Next, paste the raw data into the text field. The data should be a comma or tab separated table of matches, typically containing the chromosome number, the start and end position of the match, the number of SNPs in the match and the lenght of the match in units of centimorgans (cM). You can also drag and drop a file with the match data into the text field.

A minimal example of such a table is:

```csv
Chromosome,Start Location,End Location,Centimorgans,SNPs
6,6358001,18115715,19.6,7424
7,150135758,154205894,10.9,2816
```

If the format is valid, a preview is shown below the text field as a table. 

Finally, click on the &ldquo;Save&rdquo; button to store the match in the database.

## Viewing DNA match data

The DNA match view has a dropdown that allows to select each person in the database that has an associated DNA match. Once a person is selected, the DNA match data is shown in a table below the dropdown. It shows the name of the person the match is associated with, the relation to the person selected in the dropdown (automatically determined from the Gramps database), the total length of shared DNA in centimorgans (cM), the number of shared segments, and the length of the largest of these segments.

When you click on an individual match, it opens a detail page showing all the segments and whether the match is on the maternal or paternal side. This information can be either entered manually (by providing a `P` for paternal or `M` for maternal in a column named `Side` in the raw data) or automatically determined by Gramps based on the most recent common ancestor.

## Editing a match

You can edit a match by clicking on the pencil button in the bottom right in the match detail view. This opens a similar dialog as when creating a new match, but with the data pre-filled. Note that you can change the raw data, but not the individuals associated with the match &ndash; you need to delete the match and create a new one if you want to change the individuals.

## Working with match data in Gramps Desktop

The DNA match data is stored as a note in the Gramps database. The format is compatible with the 
[DNA Segment Map Addon](https://gramps-project.org/wiki/index.php/Addon:DNASegmentMapGramplet)
available for Gramps Desktop. Its wiki page contains more details about how to obtain the data, how to interpret it, and how to enter the data in Gramps.

!!! info
    Gramps Web API v2.8.0 introduced some changes to the accept a broader range of raw DNA match data, which is not yet available in the Gramps Desktop Addon. The Gramps Desktop Addon will be updated in the future to support the same formats as well.