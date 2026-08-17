# Synchronize Gramps Web and Gramps Desktop

*Gramps Web Sync* is an addon for Gramps that synchronizes the Gramps database on your desktop computer with Gramps Web, including media files. Changes made on either side are carried over to the other, so you can work locally and on the web on the same family tree.

Like any synchronization tool, it is not a backup: if you delete something on one side, it will be deleted on the other side too. Keep regular backups of your family tree in Gramps XML format.

## Installation

The addon requires Gramps 6.0 running on Python 3.10 or newer. It is available in Gramps Desktop and can be installed [in the usual way](https://www.gramps-project.org/wiki/index.php/5.2_Addons#Installing_Addons_in_Gramps). This documentation describes the latest version of the addon; use the Gramps addon manager to update it if needed.

Your desktop and your server must run the same version of Gramps. The version has the form `MAJOR.MINOR.PATCH`, and `MAJOR` and `MINOR` must match. See [Get Help](../help/help.md) for how to find out which Gramps version your server is running.

### Server requirements

The addon checks two things about your server as soon as it connects, before anything is downloaded, and stops with a message if either is not met:

- **Gramps Web API version 3.x.** This version of the addon, for Gramps 6.0, works with Gramps Web API 3. An older server needs updating; a server running a *newer* API major version needs a newer version of Gramps, not a newer addon, because each Gramps release line pairs with one API version. You can find the version of your server under *Settings ▸ Version info* in Gramps Web.
- **A background task queue.** Changes are applied on the server as a background task. Without a task queue, this would run synchronously and time out on any real family tree.

To apply changes to the remote database, you need an account with the role editor, owner, or administrator.

### Storing your password (optional)

Install `keyring` (e.g. `sudo apt install python3-keyring` or `sudo dnf install python3-keyring`) to store the API password in your system's password manager. If the keyring cannot be used, the addon says so and carries on without it – you will simply be asked for your password each time.

On the Gramps **Snap** package, the system keyring is blocked by confinement until you connect the interface once. The addon shows this command when it detects the situation:

```bash
snap connect gramps:password-manager-service
```

On many Gnome desktop configurations, a [bug in python keyring](https://github.com/jaraco/keyring/issues/496) means you have to create the configuration file `~/.config/python_keyring/keyringrc.cfg` with the following content:

```ini
[backend]
default-keyring=keyring.backends.SecretService.Keyring
```

## Usage

The addon is available in Gramps under *Tools ▸ Family Tree Processing ▸ Gramps&nbsp;Web&nbsp;Sync*. After confirming the dialog warning that the undo history will be discarded, the sync window opens. No changes are applied to your local tree or to the server until you explicitly confirm them.

A strip along the top of the window names the family tree you are synchronizing with, the account and address it belongs to, and when it was last synchronized. At the bottom, the version of the addon and of the server's Web API are shown, which is useful when reporting a problem.

### Connecting

If you have synchronized this family tree before and your password is stored, the addon connects as soon as it opens and goes straight to comparing. Otherwise it asks for the base URL of your Gramps Web instance (example: `https://mygrampsweb.com/`), your username, and your password.

The URL and username are stored in plain text in your Gramps user directory. The password is stored in your system password manager only if you leave **Remember password** ticked; unticking it removes any password already stored for that server. If you enter an address beginning with `http://` rather than `https://`, the addon warns you as you type, because your password would be sent in clear text.

Each server you synchronize with is stored separately, together with its own record of when it was last synchronized, so you can alternate between two servers without disturbing either. Each entry also records which local family tree it was last synchronized from. The addon only connects on its own when that matches the tree you have open; otherwise it shows the connection details and waits for you to press *Connect*.

Two actions are available while nothing is being written:

- **Change server…**, on the top strip, returns to the connection details so you can point this tree at a different server. It interrupts a comparison in progress rather than making you wait for it to finish.
- **Forget this server**, on the connection pane, removes the stored address, username and password, along with the record of when this tree last synchronized. The next synchronization then compares the two trees from scratch.

### Reviewing the changes

The addon compares the local and remote databases and shows the actions it proposes to carry out, grouped by which database they change:

```
▾ Will change on this computer (7 objects)
    ▾ Add 3 objects
        Person   John Smith        I0123
    ▾ Update 4 objects
        …
▾ Will change on the server (5 objects)
    …
```

Each row names the object, so you can tell who or what is affected rather than only seeing a Gramps ID. If anything is going to be deleted, a note above the list says how many objects and on which side.

Press **Apply** to carry out what the list describes.

The sync window does not block the rest of Gramps, so you can keep working while the list is open. If you edit an affected object in the meantime, the addon notices when you press Apply, stops without changing anything, and asks you to compare again.

#### Sync mode

The synchronization mode is selected above the list of changes. Changing it rebuilds the list, because the mode decides what each difference becomes.

- **Bidirectional synchronization** (the default) – changes from both sides are combined. Objects edited in both places are merged.
- **Reset the server to match this computer** – the server is made to match this computer. Anything changed only on the server is discarded.
- **Reset this computer to match the server** – this computer is made to match the server. Anything changed only here is discarded.

The **merge** mode available in versions before 1.5 has been removed. It differed from bidirectional synchronization only in restoring objects deleted on one side instead of propagating the deletion. If you relied on it, use bidirectional synchronization and restore anything you want to keep from a backup.

### Media files

Media files are handled as part of the same confirmation, not as a separate step. If any files need transferring, a checkbox below the list offers to move them:

```
[x] Also transfer 12 media files (4 to download, 8 to upload)
```

Untick it to synchronize the object changes without touching the files.

Files that are missing on *both* sides are listed separately, because nothing can be done about them:

```
2 media files are missing on both sides and cannot be transferred.
```

Media file synchronization has two limitations:

- If a local file has a different checksum from the one stored in the Gramps database (this can happen e.g. for Word files edited after being added to Gramps), the upload will fail with an error message.
- The tool does not verify the integrity of all local files. If a file exists under the path stored for the media object but differs from the file on the server, the tool will not detect it. Use the Media Verify Addon to find files with incorrect checksums.

### If a synchronization fails

If a synchronization fails part-way – a dropped connection, for instance – the addon reports what it had already applied and offers **Try again**, which resumes at the step that failed rather than starting over. The downloaded copy of the remote tree is kept, so retrying does not download and compare it a second time.

Technical details of the failure are available behind a *Details* expander, with a button to copy them for a bug report.

## Troubleshooting

**Unexpected changes.** If the addon proposes an alarming number of deletions, check the top strip first: it names the family tree on the server you are about to write to. Synchronizing a tree against a server holding a *different* tree produces exactly this symptom.

Otherwise, differences you did not expect can come from inconsistencies in one of the databases, or from clocks that are out of sync between your computer and your server. Check that both clocks are correctly set (the time zone does not matter, as the tool uses Unix timestamps) and run the check & repair tool on your local database. As a last resort, export your local database to Gramps XML and reimport it into a new, empty database. This is a lossless operation, but ensures all data is stored consistently.

**Media file errors.** A failed upload is often caused by a mismatch between the checksum of the file on disk and the checksum in the local Gramps database, which happens with editable files such as office documents edited outside of Gramps. Use the Gramps Media Verify Addon to correct the checksums.

**Permission errors.** Check the role of your Gramps Web user account: only editors, owners, and administrators can apply changes to the remote database.

### Ask for help

If none of the above helps, ask the community by posting in the [Gramps Web category of the Gramps forum](https://gramps.discourse.group/c/gramps-web/28). Please provide:

- the version of the Gramps Web Sync addon, shown at the bottom of the sync window next to the server's Web API version (and please use the latest released version)
- the version of Gramps desktop you are using
- the version info of Gramps Web, found under *Settings ▸ Version info*
- any details about your Gramps Web installation (self-hosted, Grampshub, ...)
- the output of your Gramps Web server logs, if you have access to them (when using Docker: `docker compose logs --tail 100 grampsweb` and `docker compose logs --tail 100 grampsweb-celery`)

If you are asked for a debug log, start Gramps [from the command line](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Command_Line) with debug logging enabled and reproduce the problem:

```bash
gramps --debug grampswebsync
```

## Background: how the addon works

The addon is meant to keep a local Gramps database in sync with a remote Gramps Web database, allowing both local and remote changes (collaborative editing).

It is **not suited**

- to synchronize with a database that is not a direct derivative (starting from a database copy or Gramps XML export/import) of the local database,
- to merge two databases with a large number of changes on both sides that need manual attention for merging. Use the excellent [Import Merge Tool](https://www.gramps-project.org/wiki/index.php/Import_Merge_Tool) for this purpose.

The principles of operation are simple:

- It compares the local and remote databases.
- If there are any differences, it checks the timestamp of the latest identical object, let's call it **t**.
- If an object changed more recently than **t** exists in one database but not the other, it is synced to both (assume new object).
- If an object changed the last time before **t** is absent in one database, it is deleted in both (assume deleted object).
- If an object is different but changed after **t** only in one database, sync it to the other one (assume modified object).
- If an object is different but changed after **t** in both databases, merge them (assume conflicting modification).

The time of the last successful synchronization is also recorded, separately for each server, and used as **t** when it is more recent than the newest identical object.

This algorithm is simple and robust as it does not require tracking synchronization history. However, it works best when you *synchronize often*.
