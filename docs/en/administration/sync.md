# Synchronize Gramps Web and Gramps Desktop

*Gramps Web Sync* is an addon for Gramps that allows to synchronize your Gramps database on your desktop computer with Gramps Web, including media files.

!!! warning
    As with any synchronization tool, please do not consider this as a backup tool. An accidental deletion on one side will be propagated to the other side. Make sure to create regular backups (in Gramps XML format) of your family tree.

!!! info
    The documentation refers to the latest version of the Gramps Web Sync Addon. Please use the Gramps addon manager to update the addon to the latest version if needed.

!!! note "What changed in version 1.5"
    The addon's interface was rewritten in version 1.5. The step-by-step wizard is gone, replaced by a single window, and media files are now confirmed together with the object changes instead of on a separate page afterwards. If you are looking for the sync mode selector, it now sits **above** the list of changes rather than below it. The **merge** sync mode has been removed; see [Sync mode](#sync-mode) below.

## Installation

The addon requires Gramps 6.0 running on Python 3.10 or newer.
It is available in Gramps Desktop and can be installed [in the usual way](https://www.gramps-project.org/wiki/index.php/5.2_Addons#Installing_Addons_in_Gramps).

!!! warning
    Please make sure to use the same version of Gramps on your desktop as the one running on your server. See the [Get Help](../help/help.md) section for how to find out which Gramps version your server is running. The Gramps version has the form `MAJOR.MINOR.PATCH`, and `MAJOR` and `MINOR` must be the same on web and desktop.

### Server requirements

The addon checks two things about your server as soon as it connects, and refuses to continue if either is not met. Both checks happen before anything is downloaded.

- **Gramps Web API version 3.x.** This version of the addon, for Gramps 6.0, works with Gramps Web API 3. An older server needs updating; a server running a *newer* API major version needs a newer version of Gramps, not a newer addon, because each Gramps release line pairs with one API version. You can find the version of your server under *Settings ▸ Version info* in Gramps Web.
- **A background task queue.** Synchronization submits its changes as a background task. On a server without a task queue configured, applying changes would run synchronously and time out on any real family tree, so the addon declines to start rather than failing part-way through.

You also need an account with at least editor privileges to apply changes to the remote database.

Optional step:

??? note inline end "Gnome keyring bug"
    There is currently a [bug in python keyring](https://github.com/jaraco/keyring/issues/496) that affects many Gnome desktop configurations.  You may need to create the configuration file `~/.config/python_keyring/keyringrc.cfg` and edit it to look like this:

        [backend]
        default-keyring=keyring.backends.SecretService.Keyring

- Install `keyring` (e.g. `sudo apt install python3-keyring` or `sudo dnf install python3-keyring`) to allow storing the API password safely in your system's password manager

If the keyring cannot be used, the addon says so and carries on without it — you will simply be asked for your password each time. On the Gramps **Snap** package the system keyring is blocked by confinement until you connect the interface once:

```bash
snap connect gramps:password-manager-service
```

The addon shows this exact command when it detects the situation.

## Usage

Once installed, the addon is available in Gramps under *Tools ▸ Family Tree Processing ▸ Gramps&nbsp;Web&nbsp;Sync*. After confirming the dialog warning that the undo history will be discarded, the sync window opens.

**No changes are applied to your local tree or to the server until you explicitly confirm them.**

The window has a strip along the top naming the family tree you are synchronizing with, the account and address it belongs to, and when it was last synchronized. At the bottom, the version of the addon and of the server's Web API are shown — useful when reporting a problem.

### Connecting

If you have synchronized this family tree before and your password is stored, the addon connects as soon as it opens and goes straight to comparing. Otherwise it asks for the base URL of your Gramps Web instance (example: `https://mygrampsweb.com/`), your username, and your password.

The URL and username are stored in plain text in your Gramps user directory. The password is stored in your system password manager only if you leave **Remember password** ticked; unticking it removes any password already stored for that server.

!!! tip "Several family trees, several servers"
    Each server you synchronize with is stored separately, together with its own record of when it was last synchronized. Alternating between two servers no longer disturbs either.

    Each entry also records **which local family tree** it was last synchronized from. The addon only connects on its own when that matches the tree you have open; otherwise it shows the connection details and waits for you to press *Connect*, with a warning if the stored credentials belong to a different tree. This matters because synchronizing a tree against a server holding a *different* tree would propose deleting the contents of both.

Two actions are available while nothing is being written:

- **Change server…**, on the top strip, returns to the connection details so you can point this tree at a different server. It interrupts a comparison in progress rather than making you wait for it to finish.
- **Forget this server**, on the connection pane, removes the stored address, username and password, along with the record of when this tree last synchronized. The next synchronization then compares the two trees from scratch.

If you enter an address beginning with `http://` rather than `https://`, a warning appears as you type. Your password would be sent in clear text, so use it only for local testing.

### Reviewing the changes

The addon compares the local and remote databases and shows what it proposes to do. Unlike earlier versions, which listed the raw differences between the two trees, the list now shows the **actions** that will be carried out, grouped by which database they change:

```
▾ Will change on this computer (7 objects)
    ▾ Add 3 objects
        Person   John Smith        I0123
    ▾ Update 4 objects
        …
▾ Will change on the server (5 objects)
    …
```

Each row names the object, so you can tell who or what is affected rather than only seeing a Gramps ID.

If anything is going to be deleted, a warning above the list says how many objects and on which side. This appears whenever deletions are involved, including during an ordinary bidirectional synchronization that is propagating a deletion you made yourself.

Press **Apply** to carry out what the list describes.

!!! warning "Do not edit while reviewing"
    The sync window does not block the rest of Gramps, so you can keep working while the list is open. If you do edit an affected object, the addon detects it when you press Apply, stops without changing anything, and asks you to compare again. Nothing is lost, but the comparison has to be repeated.

#### Sync mode

The synchronization mode is selected **above** the list of changes. Changing it rebuilds the list, because the mode decides what each difference actually becomes.

- **Bidirectional synchronization** (the default) — changes from both sides are combined. Objects edited in both places are merged.
- **Reset the server to match this computer** — the server is made to match this computer. Anything changed only on the server is discarded.
- **Reset this computer to match the server** — this computer is made to match the server. Anything changed only here is discarded.

!!! note
    The **merge** mode available in earlier versions has been removed. It differed from bidirectional synchronization only in restoring objects deleted on one side instead of propagating the deletion, which was not a distinction the interface could explain usefully. If you relied on it, use bidirectional synchronization and restore anything you want to keep from a backup.

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

Note the following limitations of the media file sync:

- If a local file has a different checksum from the one stored in the Gramps database (this can happen e.g. for Word files when edited after being added to Gramps), the upload will fail with an error message.
- The tool does not check integrity of all local files, so if a local file exist under the path stored for the media object, but the file is different from the file on the server, the tool will not detect it. Use the Media Verify Addon to detect files with incorrect checksums.

### When something goes wrong

If a synchronization fails part-way — a dropped connection, for instance — the addon reports what it had already applied and offers **Try again**, which resumes at the step that failed rather than starting over. The downloaded copy of the remote tree is kept, so retrying does not download and compare it a second time.

Technical details of the failure are available behind a *Details* expander, with a button to copy them for a bug report.

## Troubleshooting

### Debug logging

If you are encountering issues with the Sync Addon, please start Gramps with debug logging enabled by [starting Gramps from the command line](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Command_Line) with the following option:

```bash
gramps --debug grampswebsync
```

This will print many helpful logging statements to the command line that will help you identify the cause of the issue.

### Server credentials

If connecting fails, please double-check the server URL, your username and password.

### The addon refuses to connect

If the addon reports that the server's Gramps Web API version is too old or too new, or that no background task queue is configured, see [Server requirements](#server-requirements) above. These are checked before anything else, so the message names the problem directly.

### Permissions problems

If you encounter an error involving permissions, please check the user role of your Gramps Web user account. You can only apply changes to the remote database if you are a user with role editor, owner, or administrator.

### Unexpected database changes

If the sync tool detects changes that you think did not happen, it could be that there are inconsistencies in one of the databases that fool Gramps into detecting a difference, or that the time is out of sync between your local computer and your server.

Please check that the clocks on both machines are correctly set (note, the time zone does not matter as the tool uses Unix timestamps, which are time zone agnostic).

You can also run the check & repair tool on your local database and see if this helps.

A brute-force but effective method to ensure inconsistencies in your local database are not causing false positives is to export your database to Gramps XML and reimport it into a new, empty database. This is a lossless operation but makes sure all data is imported consistently.

!!! tip
    If the addon proposes an alarming number of deletions, check the top strip first: it names the family tree on the server you are about to write to. Synchronizing against a server that holds a *different* tree produces exactly this symptom.

### Timeout errors

Synchronization to the server is processed by a background worker, so long-running synchronizations should not time out. A server without a task queue configured is refused at connection time for this reason — see [Server requirements](#server-requirements).

Requests from the addon to the server time out after 60 seconds without a response, so an unreachable server reports a connection error instead of hanging indefinitely.

### Unexpected media file errors

If uploading a media file fails, it is often caused by a mismatch in the checksum of the actual file on disk and the checksum in the local Gramps database. This often happens with editable files, like office documents, edited outside of Gramps. Please use the Gramps Media Verify Addon to correct the checksums of all media files.

### Ask for help

If all the above does not help, you can ask the community for help by posting in the [Gramps Web category of the Gramps forum](https://gramps.discourse.group/c/gramps-web/28). Please make sure to provide:

- the version of the Gramps Web Sync addon (and use the latest released version please) — it is shown at the bottom of the sync window, next to the server's Web API version
- the version of Gramps desktop you are using
- the output of the Gramps debugging logging, enabled as described above
- the version info of Gramps Web (you can find it under Settings/Version info)
- any details you can provide about your Gramps Web installation (self-hosted, Grampshub, ...)
- the output of your Gramps Web server logs, if you have access to them (when using docker: `docker compose logs --tail 100 grampsweb` and `docker compose logs --tail 100 grampsweb-celery`)

## Background: how the addon works

If you are curious about how the addon actually works, you can find some more detail in this section.

The addon is meant to keep a local Gramps database in sync with a remote Gramps Web database, to allow both local and remote changes (collaborative editing).

It is **not suited**

- To synchronize with a database that is not direct derivative (starting from a database copy or Gramps XML export/import) of the local database
- To merge two databases with a large number of changes on both sides that need manual attention for merging. Use the excellent [Import Merge Tool](https://www.gramps-project.org/wiki/index.php/Import_Merge_Tool) for this purpose.

The principles of operation of the tool are very simple:

- It compares the local and remote databases
- If there are any differences, it checks the timestamp of the latest identical object, let's call it **t**
- If an object changed more recently than **t** exists in one database but not the other, it is synced to both (assume new object)
- If an object changed the last time before **t** is absent in one database, it is deleted in both (assume deleted object)
- If an object is different but changed after **t** only in one database, sync to the other one (assume modified object)
- If an object is different but changed after **t** in both databases, merge them (assume conflicting modification)

The time of the last successful synchronization is also recorded, separately for each server, and used as **t** when it is more recent than the newest identical object.

This algorithm is simple and robust as it does not require tracking synchronization history. However, it works best when you *synchronize often*.
