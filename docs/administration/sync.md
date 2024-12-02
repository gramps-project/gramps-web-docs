# Synchronize Gramps Web and Gramps Desktop

*Gramps Web Sync* is an addon for Gramps that allows to synchronize your Gramps database on your desktop computer with Gramps Web, including media files.

!!! warning
    As with any synchronization tool, please do not consider this as a backup tool. An accidental deletion on one side will be propagated to the other side. Make sure to create regular backups (in Gramps XML format) of your family tree.

Using Gramps Web Sync requires tree owner permissions in Gramps Web.

## Installation

The addon requires Gramps 5.2 running on Python 3.8 or newer.
It is available in Gramps Desktop and can be installed [in the usual way](https://www.gramps-project.org/wiki/index.php/5.2_Addons#Installing_Addons_in_Gramps).


!!! warn
    Please make sure to use the same version of Gramps on your desktop as the one running on your server. See the [Get Help](../help.md) section for how to find out which Gramps version your server is running. The Gramps version has the form `MAJOR.MINOR.PATCH`, and `MAJOR` and `MINOR` must be the same on web and desktop.


Optional step:

- Install `keyring` (e.g. `sudo apt install python3-keyring`) to allow storing the API password safely in your system's password manager 

## Usage

Once installed, the addon is available in Gramps under *Tools > Family Tree Processing > Gramps&nbsp;Web&nbsp;Sync*. Once started, and after confirming the dialog that the undo history will be discarded, the tool will ask you for the base URL (example: `https://mygrampsweb.com/`) of your Gramps Web instance, your username, and password. You need an account with owner privileges To sync changes back to your remote database. The username and URL will be stored in plain text in your Gramps user directory, the password will only be stored if `keyring` is installed (see above).

If there are any changes, the tool will display a confirmation dialog before applying the changes. (At present, the confirmation dialog only shows the Gramps IDs of the affected objects.)


## Media file synchronization

*After* the databases have been synchronized, the tool checks for any new or updated media files. It displays the files missing locally or on the remote server and, upon user confirmation, tries to download and upload the files.

Limitations:

- If a local file has a different checksum from the one stored in the Gramps database (this can happen e.g. for Word files when edited after being added to Gramps), the upload will fail with an error message.
- The tool does not check integrity of all local files, so if a local file exist under the path stored for the media object, but the file is different from the file on the server, the tool will not detect it. Use the Media Verify Addon to detect files with incorrect checksums.



## Background: how the addon works

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
