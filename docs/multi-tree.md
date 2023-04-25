By default, Gramps Web only allows accessing a single family tree database ("tree"), specified in the configuration file.

However, since version 1.0 of the Gramps Web API backend, it is also possible to serve multiple trees from a single installation. However, each user is (currently) tied to a single tree, so this setup is not suited for sharing trees among users, but for hosting multiple isolated Gramps Web instances.

## Enable multi-tree support

To enable multi-tree support, the `TREE` config option must be set to a single asterisk `*`, e.g. in a configuration file:

```python
TREE = "*"
```

This will make all trees in the server's Gramps database directory accessible (given sufficient user permissions). The tree's ID is the name of the subdirectory. You can list existing trees (names and IDs) with the command

```python
python -m gramps_webapi --config /app/config/config.cfg tree list
```

In addition, you should set the `MEDIA_PREFIX_TREE` configuration option to `True` to ensure media files are stored in separate subfolders. Otherwise, users are able to access media files that belong to a tree they have no permission for!

## Add a user account to a specific tree

To add a user to a specific tree, simply add the `--tree TREEID` command line option to the add user command. You can also POST to the `/users/` endpoint with the `tree` property set in the JSON payload.

User names and e-mail addresses are required to be unique across *all* trees.

## Create a new tree

To create a new tree, it is recommended to POST to the `/trees/` endpoint rather than using the Gramps CLI. This will use a UUIDv4 as tree ID, which leads to additional security as the name cannot be guessed. Currently, only SQLite is supported for newly created trees.


## Authorize

To authorize (fetch a token), only user name and password are necessary, like in single-tree mode, since the tree ID is known for each user, so there is no need to provide it.


## Migrate existing media files

If you want to migrate an existing Gramps Web instance to multi-tree support and are using local media files, you can simply move them to a subfolder of the original location with the tree ID as name.

If you are using media files hosted on S3, you can use the script provided in the `scripts` directory of the `gramps-webapi` repository:

```
python scripts/s3_rename.py BUCKET_NAME TREE_ID
```

This assumes the relevant access keys are set as environment variables already.


## Migrate existing user database

If you want to enable multi-tree support and reuse existing users, you need to assign them to a specific tree. You can use the following command provided for this purpose,

```python
python -m gramps_webapi --config /app/config/config.cfg user fill-tree TREE_ID
```


