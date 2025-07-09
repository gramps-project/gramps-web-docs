# Synchronize Gramps Web and Gramps Desktop

*Gramps Web Sync* is an addon for Gramps that allows to synchronize your Gramps database on your desktop computer with Gramps Web, including media files.

!!! warning
    As with any synchronization tool, please do not consider this as a backup tool. An accidental deletion on one side will be propagated to the other side. Make sure to create regular backups (in Gramps XML format) of your family tree.

!!! info
    The documentation refers to the Gramps Web Sync Addon version 1.2.1. Please use the Gramps addon manager to update the addon to the latest version if needed.

## Installation

The addon requires Gramps 5.2 running on Python 3.9 or newer.
It is available in Gramps Desktop and can be installed [in the usual way](https://www.gramps-project.org/wiki/index.php/5.2_Addons#Installing_Addons_in_Gramps).


!!! warn
    Please make sure to use the same version of Gramps on your desktop as the one running on your server. See the [Get Help](../help/help.md) section for how to find out which Gramps version your server is running. The Gramps version has the form `MAJOR.MINOR.PATCH`, and `MAJOR` and `MINOR` must be the same on web and desktop.

Optional step:

??? note inline end "Gnome keyring bug"
    There is currently a [bug in python keyring](https://github.com/jaraco/keyring/issues/496) that affects many Gnome desktop configurations.  You may need to create the configuration file `~/.config/python_keyring/keyringrc.cfg` and edit it to look like this:

        [backend]
        default-keyring=keyring.backends.SecretService.Keyring

- Install `keyring` (e.g. `sudo apt install python3-keyring` or `sudo dnf install python3-keyring`) to allow storing the API password safely in your system's password manager 

## Usage

Once installed, the addon is availabe in Gramps under *Tools > Family Tree Processing > Gramps&nbsp;Web&nbsp;Sync*. Once started, and after confirming the dialog that the undo history will be discarded, a wizard will guide you through the synchronization steps. Note that no changes will be applied to your local tree or to the server until you explicitly confirm them.

### Step 1: enter server credentials

The tool will ask you the base URL (example: `https://mygrampsweb.com/`) of your Gramps Web instance, your username, and password. You need an account with at least editor privileges to sync changes back to your remote database. The username and URL will be stored in plain text in your Gramps user directory, the password will only be stored if `keyring` is installed (see above).

### Step 2: review changes

After confirming your credentials, the tool compares the local and remote databases and assesses if there are any differences. If there are, it displays a list of object changes (where an object can be a person, family, event, place, etc.) belonging to one of the following categories:

- added locally
- deleted locally
- modified locally
- added remotely 
- deleted remotely
- modified remotely
- modified simultaneously (i.e., on both sides)

The tool uses time stamps to assess which side is newer for each object (see "Background" below if you are interested in the details).

If the changes look as expected, you can click "Apply" to apply the necessary changes to the local and the remote databases.

!!! tip "Advanced: Sync mode"
    Below the list of changes, you can select a synchronization mode.
    
    The default, **bidirectional synchronization**, means that it will apply changes to both sides (local and remote) by replicating the detected changes (objects added locally will be added on the remote side, etc.). Objects modified on both sides will be merged and updated on both sides as well.

    The option **reset remote to local** will instead ensure the remote Gramps database looks exactly like the local one. Any objects detected as "added remotely" will be deleted again, objects detected as "deleted remotely" will be added again", etc. *No changes will be applied to the local Gramps database.*

    The option **reset local to remote** works in the opposite way and sets the local state to the one of the remote database. *No changes will be applied to the remote database.*

    Finally, the option **merge** is similar to biderectional synchronization in that it modifies both databases, but it *does not delete any objects*, but instead restores all objects deleted on only one side.


### Step 3: synchronize media files

*After* the databases have been synchronized, the tool checks for any new or updated media files. If it finds any, it displays a list and asks for confirmation to upload/download the necessary files.

Note the following limitations of the media file sync:

- If a local file has a different checksum from the one stored in the Gramps database (this can happen e.g. for Word files when edited after being added to Gramps), the upload will fail with an error message.
- The tool does not check integrity of all local files, so if a local file exist under the path stored for the media object, but the file is different from the file on the server, the tool will not detect it. Use the Media Verify Addon to detect files with incorrect checksums.


## Troubleshooting

### Debug logging

If you are encountering issues with the Sync Addon, please start Gramps with debug logging enabled by [starting Gramps from the command line](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Command_Line) with the following option:

```bash
gramps --debug grampswebsync
```

This will print many helpful logging statements to the command line that will help you identify the cause of the issue.

### Server credentials

If the first step already fails, please double-check the server URL, your username and password.

### Permissions problems

If you encounter an error involving permissions, please check the user role of your Gramps Web user account. You can only apply changes to the remote database if you are a user with role editor, owner, or administrator.

### Unexpected database changes

If the sync tool detects changes that you think did not happen, it could be that there are inconsistencies in one of the databases that fool Gramps into detecting a difference, or that the time is out of sync between your local computer and your server.

Please check that the clocks on both machines are correctly set (note, the time zone does not matter as the tool uses Unix timestamps, which are time zone agnostic).

You can also run the check & repair tool on your local database and see if this helps.

A brute-force but effective method to ensure inconsistencies in your local database are not causing false positives is to export your database to Gramps XML and reimport it into a new, empty database. This is a lossless operation but makes sure all data is imported consistently.

### Timeout errors

If you are experiencing timeout errors (e.g. indicated by a HTTP status 408 error or another error message including the word "timeout"), it is likely due to a large number of changes that need to be synchronized to the remote side in combination with your server setup.

For versions of the sync addon earlier than v1.2.0 and versions of Gramps Web API earlier than  v2.7.0 (see the version info tab in Gramps Web), synchronization to the server side was processed in a single request that would time out, depending on the server configuration, after one to at most a few minutes. For large syncs (such as after importing thousands of objects in the local database or attempting to sync a full local database to an empty server side database), this can be too short.

If you are using the sync addon v1.2.0 or later and Gramps Web API v2.7.0 or later, server-side synchronization is processed by a background worker and can run for very long (a progress bar will be displayed) and timeout errors should not occur.

### Unexpected media file errors

If uploading a media file fails, it is often caused by a mismatch in the checksum of the actual file on disk and the checksum in the local Gramps database. This often happens with editable files, like office documents, edited outside of Gramps. Please use the Gramps Media Verify Addon to correct the checksums of all media files.

### Ask for help

If all the above does not help, you can ask the community for help by posting in the [Gramps Web category of the Gramps forum](https://gramps.discourse.group/c/gramps-web/28). Please make sure to provide:

- the version of the Gramps Web Sync addon (and use the latest released version please)
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

This algorithm is simple and robust as it does not require tracking synchronization history. However, it works best when you *synchronize often*.
