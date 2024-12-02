# Create an account for the tree owner

Before you can start using Gramps Web, you need to create an account for the tree owner. If no user account exists for a given tree, a form will be shown to create an account. The form depends on the server setup being for a single tree or for multiple trees.

## Single-tree setup: create admin account

On a server with single-tree setup, when no user account exists yet, opening Gramps Web shows a form to create an admin account. The admin user will be both the owner of the (single) tree and the administrator of the installation. The form also allows setting the e-mail configuration needed for e-mail notifications (e.g. resetting a user password). If the e-mail configuration has already been added via a configuration file or environment variables on the server, this part of the form can be left empty.

The form also allows to import genealogical data by uploading a file. This can also be done later from the "Import" page in Gramps Web (see [Import data](import.md)).

## Multi-tree setup: create admin account

In a multi-tree setup, the same form to create an admin account will be shown if no users exists *in any tree*, i.e. when the server has just been created.

## Multi-tree setup: create tree owner account

In a multi-tree setup, every user is tied to a single tree. Even if users already exist in other trees, a tree owner can be created in the web interface if no owner exists *for this tree* yet.

However, the owner creation form will not be displayed automatically on the Gramps Web home page, which is the same for all trees. Instead, it can be reached at `https://my-gramps-instance/firstrun/my-tree-id`, where  `https://my-gramps-instance` is the base address of your Gramps Web installation, and `my-tree-id` is the ID of your tree.

A possible workflow for a site administrator to create a new tree is to

- Create a tree via the REST API, obtaining the tree ID of the new tree
- Share the link to the owner creation form with the appropriate tree ID with the prospective tree owner

The tree owner creation form is analogous to the admin creation form described above, except that it does not allow to change the e-mail configuration (which is only allowed for admins).