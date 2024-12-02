# User system

Gramps Web is not meant to be exposed to the internet for public access, but only by authenticated users. User accounts can be created by the site owner via the command line or web interface, or by self-registration and subsequent approval by the site owner.

## User roles

The following user roles are currently defined.

Role | Role ID | Permissions
-----|---------|------------
Guest | 0 | View non-private objects
Member | 1 | Guest + view private objects
Contributor* | 2 | Member + add objects
Editor | 3 | Contributor + edit and delete objects
Owner | 4 | Editor + manage users
Admin | 5 | Owner + edit other trees in multi-tree setup

\* Note that the "Contributor" role is currently only partially supported; e.g., family objects cannot be added since they imply a modification of the underlying Gramps person objects of family members. It is recommended to use the other roles whenever possible.

## Configuring who can use AI chat

If you have [configured AI chat](chat.md), you will see an option here to choose which user groups are allowed to use the chat feature.

## Managing users

There are two ways to manage users:

- With owner permissions using the web interface
- On the command line on the server

The owner account required to first access the web app can be added in the onboarding wizard that is automatically launched when accessing Gramps Web with an empty user database.

### Managing users on the command line

When using [Docker Compose](install_setup/deployment.md), the basic command is

```bash
docker compose run grampsweb python3 -m gramps_webapi user COMMAND [ARGS]
```

The `COMMAND` can be `add` or `delete`. Use `--help` for `[ARGS]` to show the syntax and possible configuration options.

### Approving self-registered users

When a user self-registers, they are not granted immediate access. An email is sent to the tree owner about the new user registration and the user is sent an email request to confirm their email address. Successfully confirming their email address changes their role from `unconfirmed` to `disabled`. While the user account is in either of those two roles, the user cannot log in. The tree owner must review the user's request and assign the user an appropriate role before they are allowed to log in.
