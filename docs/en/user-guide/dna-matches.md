# Working with DNA matches

DNA matches are segments of DNA that agree between two individuals, identified by the presence of markers, so-called SNPs (the acronym for single nucleotide polymorphisms, pronounced &ldquo;snips&rdquo;).

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

The DNA match view has a dropdown that allows to select each person in the database that has an associated DNA match. Once a person is selected, their matches are listed in a table: the name of the match, their relationship to the selected person, the total length of shared DNA in centimorgans (cM), the number of shared segments, and the length of the largest of these segments.

For matches that are already placed in the tree, the relationship column shows the relationship recorded in the tree (automatically determined from the Gramps database). For matches who are not related to the selected person in the tree, it shows the relationship estimated from the shared DNA, marked with "≈".

Clicking a match opens its page, with a summary of the shared DNA, the [relationship estimate](#relationship-estimate), a chart of the relationship in the tree, and the list of segments. Each segment shows whether it is on the paternal or maternal side. The side can either be entered manually (by providing a `P` for paternal or `M` for maternal in a column named `Side` in the raw data) or determined automatically from the most recent common ancestor. The download button next to the segments saves them as a CSV file in the format the match dialog accepts.

## Relationship estimate

Shared DNA is not proof of a specific relationship: the amount of DNA two relatives share varies a lot, and different relationships overlap. Gramps Web therefore shows a range of possible relationships with their probabilities, computed from the number and lengths of the shared segments (requires Gramps Web API 3.26 or newer).

Relationships are grouped by their *degree*:

- **Parent or child** and **Full sibling** are shown on their own.
- **Relative of degree 2** includes half siblings, grandparents and grandchildren, and aunts, uncles, nieces, and nephews.
- **Relative of degree 3** includes first cousins, great-grandparents, great-aunts and great-uncles, and half aunts and uncles.
- Each further degree is about one generation further apart, e.g. first cousins once removed are degree 4 and second cousins are degree 5. Degree 9 and beyond are grouped as "9+".

Relationships with the same degree share about the same amount of DNA on average, so DNA alone cannot tell them apart. Use the ages of the people to decide between them – a 30-year-old relative of degree 2 of a 60-year-old is more likely a niece than a grandparent.

The estimate is most reliable for close relatives. For distant relationships, matches share only few segments, and the probabilities spread over several degrees.

### Checking the tree against the DNA

If the match is placed in the tree, Gramps Web checks whether the shared DNA fits the relationship recorded there. If the DNA is very unlikely for that relationship, a warning icon is shown in the matches table and a warning on the match page. The number in brackets, e.g. "1 : 500", compares how likely the DNA is for the recorded relationship with how likely it is for the most likely relationship.

A warning is a reason to look more closely, not proof of an error. Common causes are:

- a mistake in the tree, such as a wrong parent,
- a misattributed parentage, e.g. an unknown adoption or a different biological father,
- incomplete match data, for example if only segments above a high threshold were copied from the testing service,
- relationships through more than one line, e.g. people related through both their mother and father ("pedigree collapse"), which share more DNA than expected.

Relationships that are not by birth, such as through an adoption, are not checked.

## Editing a match

To edit a match, open its page and click the edit button, or press `e`. Note that you can change the raw data, but not the individuals associated with the match – you need to delete the match and create a new one if you want to change the individuals.

## Private matches

The dialogs for adding and editing a match have a **Private** switch. A private match, including its segments, is hidden from users who can't view private records. Private matches are marked with a lock for everybody else. See [Private records](privacy.md) for more about privacy.

## Working with match data in Gramps Desktop

The DNA match data is stored as a note in the Gramps database. The format is compatible with the 
[DNA Segment Map Addon](https://gramps-project.org/wiki/index.php/Addon:DNASegmentMapGramplet)
available for Gramps Desktop. Its wiki page contains more details about how to obtain the data, how to interpret it, and how to enter the data in Gramps.

!!! info
    Gramps Web API v2.8.0 introduced some changes to the accept a broader range of raw DNA match data, which is not yet available in the Gramps Desktop Addon. The Gramps Desktop Addon will be updated in the future to support the same formats as well.
