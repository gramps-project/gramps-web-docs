# How Gramps organizes data

Gramps Web stores a family tree not as a chart, but as separate objects – people, families, events, places, sources, and so on – that are linked to each other. Once you know how these objects fit together, entering data becomes predictable: anything you want to link to has to exist first.

Gramps Web uses the same data model as Gramps Desktop, so everything on this page applies to both.

## The building blocks

| Object | What it represents | Examples |
|---|---|---|
| Person | An individual | You, your grandmother |
| Family | A couple, their children, or both | Your parents and their children |
| Event | Something that happened, with a date and a place | Birth, marriage, census, emigration |
| Place | A geographic location | A village, a parish, a country |
| Source | A document or collection of information | A parish register, a census, a book |
| Citation | A specific reference within a source | Page 12, entry 3 of the parish register |
| Repository | Where a source is kept | An archive, a library, a website |
| Note | Free text | A transcription, research remarks |
| Media object | A file | A photo, a scanned certificate |

Every object type has its own list in Gramps Web, see [Lists](lists.md).

## People and families

Parents and children are not linked to each other directly, but through a **family**. A family has up to two partners and any number of children:

- Your parents and you are linked through the family in which you are a child.
- Your siblings are the other children of the same family.
- You and your spouse form another family, in which you are a partner, together with your children.

A person can be a child in one family and a partner in several. Each child has a relationship to each of the parents, such as birth, adoption, or stepchild, and each family has a relationship type, such as married or civil union.

This is why "adding parents" to a person means adding the person as a child to a family – which the [tree chart](tree-edit.md) does for you in one step.

## Events

A birth, death, or marriage is not a field of a person, but an **event** of its own, with a type, a date, a place, and a description. People are linked to an event with a **role**: the person whose birth it is has the role "Primary", while someone else might be linked to the same event as a witness.

Events that concern a couple, such as a marriage, belong to the family rather than to either partner. An event can also be shared by several people – for example a census record listing a whole household – instead of being entered once per person.

## Shared objects: places and sources

Places, sources, citations, repositories, notes, and media objects exist in their own right, and any number of other objects can refer to the same one. This has a few consequences:

- **Create once, select many times.** The village where ten of your ancestors were born is one place, selected in ten birth events. If you correct its name or coordinates, the correction applies everywhere.
- **Create it before you select it.** Forms in Gramps Web select places and sources that already exist. Create a new place or source first using the **+** (Add) button in the top app bar.
- **Places are nested.** A place can be enclosed by a larger one – a village by a county, the county by a country – so you don't have to repeat the whole hierarchy for every village.
- **Sources and citations are separate.** A source is the parish register as a whole; a citation is the specific entry that supports a fact, with its page, date, and your confidence in it. Many citations can point to the same source.

If you have accidentally created the same place or source twice, you can [merge the duplicates](lists.md#merge).

## The Home Person

The Home Person is the person the family tree charts start from and the default starting point for reports. See [First login](first-login.md) for how to set it.

!!! note "Different from Gramps Desktop"
    In Gramps Desktop, the Home Person is stored in the family tree database, so it is the same for everyone who opens that database. Gramps Web does not use it. Instead, the Home Person is stored in your browser, separately for each tree: it is not shared with other users, and it does not follow you to a different browser or device. After importing a tree from Gramps Desktop, or when you use Gramps Web on another device, you have to set it again.

## A recommended order

When entering a new family by hand, this order avoids jumping back and forth between forms:

1. **Places and sources.** Create the places you need and, if you record sources, the source you are working from.
2. **People.** Add the people with their birth and death dates and places. This is fastest in the edit mode of the Family Tree chart, which creates the families for you – see [Start a new tree](start-tree.md) and [Editing the family tree](tree-edit.md).
3. **Further events.** Open a family (for example from a person's Relationships tab) to add the marriage, and a person's page to add other events.
4. **Citations.** On the Source Citations tab of the person, event, or other object that a source supports, add a new citation, select the source, and enter the page.
5. **Notes and media.** Attach transcriptions, photos, and scans – see [Add media files](media.md).

## Entering dates

A date is entered as separate year, month, and day fields, which can also be filled in using a date picker. Leave out the parts you don't know: a year alone is a valid date.

Instead of guessing an exact day, describe what you actually know with the date's **Type**:

| What you know | Type | Example |
|---|---|---|
| The exact date, or part of it | Regular | 12 March 1850, or just 1850 |
| An approximate date | about | about 1850 |
| A limit | before, after | before 1900 |
| The date lies somewhere within a period | Range | between 1850 and 1855 |
| Something lasted for a period | Span | from 1850 to 1855 |
| Only the start or end of a period | from, to | from 1850 |

The **Quality** field records how you arrived at a date: "Estimated" for an educated guess, "Calculated" for a date derived from other information, such as a birth year calculated from an age at death.

!!! warning "About and estimated dates cover 50 years either way"
    When Gramps compares dates, it treats a date of the type "about" – and any date with the quality "Estimated" – as a range reaching from 50 years before to 50 years after the given date. For example, filtering the People list for people born between 1840 and 1860 also finds a person born "about 1880", because that date is taken to cover 1830 to 1930. In the same way, "before" and "after" are taken to reach up to 50 years before or after the date.

    This can lead to surprising results, so use "about" and "Estimated" only when you can't narrow the date down. If you know a shorter period, a Range such as "between 1878 and 1882" is more precise.

The **Calendar** field lets you enter a date in the calendar used in the original record, such as the Julian calendar, instead of converting it yourself.
