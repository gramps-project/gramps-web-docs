# Revision History

The revision history view shows all edits that have been made to the family tree.

The list view shows the edits grouped by "transactions". A transaction is a group of one or more additions, deletions, or changes to Gramps objects. For instance, adding a new family with two existing persons as father and mother generates a transaction with one added family object and two modified person objects (because they contain the link to the new family object).

Clicking on a transaction opens the transaction detail view. It contains the list of individual additions, deletions, and updates by Gramps object.

Selecting an indivdial change opens a view of the raw JSON representation of the Gramps object with additions and deletions highlighted in green and red, respectively.

## Undoing a revision

On the transaction detail page, an **Undo** button allows you to reverse that transaction. Clicking it checks whether the undo can be performed cleanly.

**Clean undo** – if none of the objects affected by the transaction have been modified since, the undo can proceed without risk. A confirmation dialog is shown and clicking **Undo** reverses the transaction.

**Force required** – if one or more affected objects have been modified by a later transaction, a clean undo is not possible. The dialog warns that forcing the undo may result in data inconsistencies, since later changes that depend on the objects in question will be preserved as-is even though the underlying objects are being reverted. You can then either cancel or click **Force undo** to proceed anyway.

In both cases the undo runs as a background task and a progress indicator is shown.