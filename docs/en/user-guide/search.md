# Search

The search page is accessible by clicking the magnifying glass icon in the top app bar, or by pressing the `s` [keyboard shortcut](shortcuts.md).

## Full-text search

Type a query into the search field. Results appear as you type, from the second character on; press Enter to search for a single character. Gramps Web searches across all object types – people, families, events, places, sources, citations, repositories, notes, and media – and returns matching results ranked by relevance. To clear the search, click the clear button in the field or press Escape.

Each result shows the object type, its name, and some details, for example the birth and death of a person, the marriage of a family, the author of a source, or the first line of a note. Click any result to open the corresponding detail page.

## Search syntax

- **All words must match.** `Müller Berlin` finds objects that contain both words.
- **`or`** finds objects that contain either word, e.g. `Meyer or Maier`. `and` can be typed between words too, but it makes no difference.
- `or` applies to the words directly next to it: `Meyer or Maier Berlin` means "(Meyer or Maier) and Berlin". Parentheses are not supported.
- **Quotes** match a phrase, i.e. words in this order: `"Johann Georg"`.
- **Wildcard:** a trailing `*` matches any ending, e.g. `Mey*` matches "Meyer", "Meyers", "Meyerhofer", etc. This also works for phrases: `"Johann Georg"*`.
- **The last word is completed.** If the query ends in a letter or digit, it is searched as if it ended in `*`, so `Anna Smi` already finds "Anna Smith". To search for the last word exactly, end the query with a space, or put the word in quotes. The same applies to the search boxes of the object selectors and the [map](map.md#search).
- `or` and `and` are recognized in any case. To search for one of these words itself, put it in quotes.
- Words cannot be excluded; there is no "not".

## What the search finds

- Accents don't need to match: "Müller" also finds "Muller", and "muller" finds "Müller".
- Families and events are also found by the names of their people, e.g. "Müller" finds the families and events of everyone named Müller. These results are ranked below direct matches.
- Standard types are found by their names in your interface language, e.g. "Taufe" finds baptisms in the German interface.
- Underscores separate words, so "microfilm" finds a media file named `scanned_microfilm.png`.
- Users who can't view private records don't find objects through private information, such as a family through the name of a private member.

## Filtering by object type

Below the search field, toggle buttons for each object type (People, Families, Events, Places, …) let you narrow results to one or more specific types. By default all types are searched. Activating one or more toggles restricts results to those types only.

