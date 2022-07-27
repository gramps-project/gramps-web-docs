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
Owner | 4 | All: Editor + manage users

\* Note that the "Contributor" role is currently only partially supported; e.g., family objects cannot be added since they imply a modification of the underlying Gramps person objects of family members. It is recommended to use the other roles whenever possible.

## Managing users

There are two ways to manage users:

- With owner permissions using the web interface
- On the command line on the server

The owner account required to first access the web app can be added in the onboarding wizard that is automatically launched when accessing Gramps Web with an empty user database. 

### Managing users on the command line

When using [Docker Compose](Deployment.md), the basic command is

```bash
docker-compose run grampsweb python3 -m gramps_webapi user COMMAND [ARGS]
```

The `COMMAND` can be `add` or `delete`. Use `--help` for `[ARGS]` to show the syntax and possible configuration options.
