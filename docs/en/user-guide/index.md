---
hide:
  - toc
---

# User Guide

This section documents the features available to users of Gramps Web.

!!! note "Not seeing all features?"
    Gramps Web uses a role-based permission system. Some features – such as editing data, managing tags, or viewing private records – are only available to users with sufficient permissions. You can check your current role in [User Settings](settings.md). If you need more access, contact your tree owner or administrator. See [User system](../install_setup/users.md) for a description of all roles.

## Navigating the interface

### Main navigation

The sidebar (or hamburger menu on mobile) is the primary way to move between sections:

- **Home** – the dashboard (see below)
- **Blog** – family history stories written as blog posts
- **Family Tree** – interactive tree charts
- **Timeline** – chronological view of events across the tree (requires a sufficiently recent Gramps Web API version)
- **Map** – geographic view of places in the tree
- **DNA** – DNA match analysis tools
- **Lists** – browse all objects of each type: People, Families, Events, Places, Sources, Citations, Repositories, Notes
- **Media** – browse all media files (photos, documents, etc.)
- **Assistant** – AI chat assistant (if enabled by the administrator)
- **History** – recently changed objects
- **Bookmarks** – your saved bookmarks
- **Tasks** – research tasks
- **Reports** – generate reports
- **Export** – export the family tree
- **Revisions** – full transaction history (visible to members and above)
- **Notifications** – past notifications

!!! note
    Tags are no longer managed from the sidebar – tag management has moved to [Administration Settings](../administration/settings.md#tags) (Owner/Administrator only). See [Tags](tags.md) for how tags are used.

### Top app bar

The bar at the top of every page contains:

- **Add** (plus icon, visible to contributors and above) – opens a menu to create a new object: Person, Family, Event, Place, Source, Citation, Repository, Note, Media Object, or Task
- **Search** (magnifying glass) – opens the search page
- **User icon** – opens the settings menu: User Settings, Administration (owners only), Manage Users (owners only), System Info

## The home page (dashboard)

The dashboard is shown when you first log in. It has two columns:

**Left column:**

- **Home person card** – shows the name, photo (if available), and key facts of your chosen home person, with a link to their full profile and quick navigation to the family tree. Click the **Set Home Person** button on the card to search for and select a different person.
- **Anniversaries** – upcoming birthdays and anniversaries from the tree, based on today's date.
- **Recently changed** – a short list of the most recently modified objects, useful for tracking collaborative edits.

**Right column:**

- **Recent blog posts** – the latest entries from the [blog](blog.md), if any exist.
- **Statistics** – a summary of object counts in the tree (number of people, families, events, etc.).

If the tree administrator has configured a **home page note** and/or a **home page image**, these are displayed prominently above the main columns. The image appears beside the note text when both are set. See [Administration Settings](../administration/settings.md#customization) for how to configure these.

!!! tip
    If the tree is empty and you have edit permissions, the dashboard shows a "Get started" prompt with buttons to add your first person or import a family tree file.
