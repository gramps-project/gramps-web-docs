# Private records

Any record in the tree can be marked as private. Together with the [user roles](../install_setup/users.md#user-roles), this decides who sees what.

## Who can see what

Gramps Web is never open to the public: only users with an account can see anything. "Public" in Gramps simply means "not private", i.e. visible to every logged-in user of the tree.

| Role | Public records | Private records |
|---|---|---|
| Guest | view | – |
| Member | view | view |
| Contributor | view, add | view, add |
| Editor, Owner, Administrator | view, add, edit, delete | view, add, edit, delete |

For guests, private records don't exist: they are left out of pages, lists, search results, charts, reports, exports, and AI assistant answers. This is enforced where the server reads the database, not by hiding things in the app, so a guest cannot get to private data in any other way either.

Accounts that have not been approved yet (after [self-registration](registration.md)) cannot log in at all.

So if relatives or other people with a guest account should not see certain information, mark it as private. If all users of a tree may see everything, give them the member role (or higher) and there is no need to mark anything as private.

## Living people are not private automatically

Nothing is made private automatically – not even people who are still alive. Data of living people is visible to guests until you mark it as private. This also applies to imported trees.

To make the people who are probably alive private in Gramps Web:

1. In the people list, open the [advanced filter](lists.md#advanced-filter) and add the condition "People probably alive" (leave the date empty for today). Apply the filter.
2. Click **Select**, tick the checkbox in the header, and choose **Select All**.
3. Choose the **Privacy** action and mark the records as private.

"Probably alive" is estimated from the dates of the person and their relatives. People without any usable dates are considered alive. Check the result, and keep in mind that the estimate can change as you add data.

Marking a person as private hides the person, but not their events, notes, media, or families – see below. Gramps Desktop has more tools to set the privacy of many related records at once, which you can use with the [Sync addon](../administration/sync.md).

People who die later don't become public automatically either. Whether you want that is up to you – many researchers prefer to keep collected information private for some time.

## Reading the lock icons

Users who can view private data see a lock next to private items. There are two kinds:

- **Filled lock** – the record itself is private. On a person's page, for example, a filled lock next to an event means the event is private, and next to a child that the child is private.
- **Outline lock** – only the *link* is private, not the record it leads to. For example, a person's link to an event can be private while the event itself is public. The event is then hidden from that person's page but still visible elsewhere, such as on the pages of other participants or in the event list.

If both the record and its link are private, the filled lock is shown.

The same distinction applies to children (the child or the child's link to the family), associations, repository links of a source, and media in a gallery. Names, attributes, addresses, and URLs belong to their record and only have the filled lock.

## Making something private

You need edit permissions to change privacy.

- **A whole record**: open its page, enter edit mode, and click the lock button in the toolbar.
- **Part of a record** – an alternate name, attribute, address, URL, association, child link, or repository link: open the edit dialog of that item and turn on the **Private** switch. The primary name has no switch, since the person would otherwise show as "Private".
- **An event from a person's or family's page**: the event's edit dialog has a privacy switch for the event itself. If the event is shared with other people, it only becomes editable after **Edit for everyone**, since it is private for all of them.
- **A person's link to an event**: on the event page, open the participant's row in edit mode. The privacy switch there applies only to that participant's link, so the event stays visible for the other participants.
- **A media object in a gallery**: in edit mode, click the lock in the corner of the tile.
- **Many records at once**: select them in a list and use the **Privacy** action, see [Lists](lists.md#tags-and-privacy).

To check which records in a list are private, turn on the **Privacy** column in the column picker of the list.

## Things to keep in mind

- Making a record private does not make the records it links to private. If a person is private, their events, the families they belong to, and the notes attached to them are still visible unless they are private themselves. Use the advanced filter or the **Privacy** column to check related records.
- Making a family or event private hides it, but not the people in it.
- [DNA matches and Y-DNA data](dna-matches.md#private-matches) have their own **Private** switch in their dialogs.
- Exports and media archives made by a user who cannot view private data contain no private records or files.
- Privacy is a Gramps feature, so records marked as private in Gramps Desktop are private in Gramps Web as well, and vice versa.
