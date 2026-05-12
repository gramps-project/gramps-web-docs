# Manage Users

The user management interface is accessible via **Settings > Manage Users** (the user icon in the top app bar). It is only available to users with the Owner or Administrator role.

## User roles

See [User system](../install_setup/users.md) for a full description of the available user roles and their permissions.

## View and filter users

The manage users page shows a table of all registered user accounts with the following columns:

- **Username** — the login name
- **Full Name** — the display name
- **E-mail** — the user's e-mail address
- **Role** — the assigned role (Guest, Member, Contributor, Editor, Owner, or Administrator)
- **Account Source** — either "Password" (local account) or the name of an external identity provider (e.g. when using OIDC)

Use the search field and role drop-down at the top of the table to filter the list. Click the filter-clear button to reset all filters.

## Edit a user

Click the edit (pencil) icon on any row to open the edit dialog. You can change the user's:

- Full name
- E-mail address
- Role

This is the primary way to **enable a newly self-registered user**: change their role from *disabled* to any active role (e.g. Member or Editor).

## Add a user manually

Click the **add user** (person-add) icon above the table to create a new user account directly without requiring self-registration. Fill in the username, full name, e-mail address, password, and role in the dialog and click **Save**.

## Delete a user

Click the delete (trash) icon on any row and confirm the dialog. This action cannot be undone.

## Export and import user accounts

These buttons are useful when [migrating to a different Gramps Web instance](export.md).

- **Export user details** (download icon) — downloads a JSON file containing all user accounts (without passwords, since passwords are stored in encrypted form).
- **Import user accounts** (group-add icon) — uploads a previously exported JSON file to create user accounts in bulk. All imported users will need to set a new password via the "Forgot password" link, since passwords cannot be transferred.

## Registration link (multi-tree setup only)

In a multi-tree setup the registration link for new users is shown at the top of the manage users page. You can copy this link and share it with people you want to invite to register an account on your tree.

!!! note
    In a single-tree setup there is a generic "Register" link on the login page; the per-tree registration link is only needed in multi-tree installations.

## AI chat permissions

If AI chat has been enabled on the server, a drop-down at the top of the page lets you control which user roles are allowed to use the chat feature:

- Everybody (including guests)
- Member and above
- Contributor and above
- Editor and above
- Owners and administrators only
- Nobody (disable chat for all users)
