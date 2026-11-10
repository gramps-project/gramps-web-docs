# Use the built-in task management

Gramps Web contains a built-in genealogical task management tool. It is meant to enable researchers to plan and prioritize, but also document their tasks. This is why tasks are represented as sources in the Gramps database. After completing a task, the associated content can serve as a source documenting the research process.

## Task basics

Tasks have the following properties:

- Status. This can be "Open", "In Progress", "Blocked", or "Done"
- Priority. This can be "Low", "Medium", or "High"
- Tags. The labels are normal Gramps tags of the underlying source. (Note that all tasks additionally have the `ToDo` label to identify them as tasks, but this label is hidden in the task list to avoid clutter.)
- Title. Shown in the task list
- Description. A rich-text field that can be used to describe the problem statement, but also document any progress made
- Media. Any media files attached to the task

## Create a task

Since tasks are normal Gramps objects, they can be edited or created by the same group of users that can edit or create other objects (like people or events).

To create a task, click on the + button on the task list page. Enter at least a title, and optionally a priority, a description, attachments, and tags. The status will always be "Open" on creation.

## The task list

The task list is sorted by status – done tasks last – and within each status by priority, highest first.

Click a task to open it. Users with edit permissions can also click the status icon of a task to change its status directly in the list, for example to mark it as done.

The **filter** button above the list filters the tasks by tag, with a [GOQL](goql.md) expression, or with the [advanced filter](lists.md#advanced-filter).

## Edit a task

The task page does not have a separate "edit mode" like other Gramps objects:

- Click the title to edit it. Press Enter, click ✓, or click elsewhere to save; press Escape or click ✕ to cancel.
- Changes to the status and priority are applied immediately.
- To edit the description or the attachments, click the edit button next to the heading of the section. The description is saved with the "save" button beneath it; editing attachments ends with **Done**.
- The lock button sets whether the task is private. The task's description gets the same privacy.

Users without edit permissions see the status and priority as text, and sections without content are hidden.

Below the title, editors see two more buttons: **Edit Source** opens the source that represents the task, where its other notes, citations, and attributes can be edited. **Delete** deletes the task after a confirmation and returns to the task list; the message that appears has an undo button to restore the task.

## Bulk change of task properties

Users with edit permissions see a checkbox on each row of the task list. Select tasks and use **Set Priority** or **Set Status** above the list to change all selected tasks at once.

## Tasks in Gramps Desktop

When adding tasks via Gramps Web, both the sources and the notes will have the `ToDo` tag attached to them, so the tasks will show up in the desktop [To Do Notes Gramplet](https://gramps-project.org/wiki/index.php/Addon:ToDoNotesGramplet) as well as the [To Do Report](https://gramps-project.org/wiki/index.php/Addon:ToDoReport).

To add or edit a task in Gramps Desktop, use the following guidelines

- Add a source with tag `ToDo` and the task title as title
- Optionally, add a note to the source with tag `ToDo`, type "To Do", and the description as text
- Add an attribute "Status" and set it to "Open", "In Progress", "Blocked", or "Done"
- Add an attribute "Priority" and set it to 9 for low, 5 for medium, or 1 for high (these counter-intuitive values are taken from the iCalendar specification)
