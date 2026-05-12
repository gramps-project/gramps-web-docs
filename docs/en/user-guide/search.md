# Search

The search page is accessible by clicking the magnifying glass icon in the top app bar, or by pressing the `s` [keyboard shortcut](shortcuts.md).

## Full-text search

Type any query into the search field and press Enter (or click the search button). Gramps Web searches across all object types – people, families, events, places, sources, citations, repositories, notes, and media – and returns matching results ranked by relevance.

Results show the object type, name, and a brief summary. Click any result to open the corresponding detail page.

A trailing `*` can be used as a wildcard, e.g. `Mey*` matches "Meyer", "Meyers", "Meyerhofer", etc.

## Filtering by object type

Below the search field, toggle buttons for each object type (People, Families, Events, Places, …) let you narrow results to one or more specific types. By default all types are searched. Activating one or more toggles restricts results to those types only.

## Semantic search

If the server administrator has enabled [semantic (AI-powered) search](../install_setup/configuration.md), a mode toggle appears in the top-right corner of the search page with two options:

- **Search** – standard full-text search (the default)
- **Semantic** – AI-powered search that understands the meaning of your query rather than matching exact words

Semantic search is useful for natural-language queries such as "farmer in Bavaria in the 19th century". It requires the semantic search index to be populated; see [Administration settings](../administration/settings.md) for how to build or update the index.

