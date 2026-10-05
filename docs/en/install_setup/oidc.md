# OIDC Authentication

Gramps Web supports OpenID Connect (OIDC) authentication, allowing users to log in using external identity providers. This includes the built-in providers Google and Microsoft, as well as custom OIDC providers like Keycloak, Authentik, and Authelia.

!!! warning "GitHub as an OIDC provider is no longer supported"
    If you have `OIDC_GITHUB_CLIENT_ID` / `OIDC_GITHUB_CLIENT_SECRET` set from an earlier version, remove them – they are now ignored, and users who previously signed in via GitHub can no longer log in that way. GitHub is an OAuth 2.0 provider, not an OpenID Connect provider, and never returned the claim Gramps Web relies on for identity, so it was never fully reliable.

## Overview

OIDC authentication allows you to:

- Use external identity providers for user authentication
- Support multiple authentication providers simultaneously
- Map OIDC groups/roles to Gramps Web user roles
- Implement Single Sign-On (SSO) and Single Sign-Out
- Optionally disable local username/password authentication

## Configuration

To enable OIDC authentication, you need to configure the appropriate settings in your Gramps Web configuration file or environment variables. See the [Server Configuration](configuration.md#settings-for-oidc-authentication) page for a complete list of available OIDC settings.

!!! info
    When using environment variables, remember to prefix each setting name with `GRAMPSWEB_` (e.g., `GRAMPSWEB_OIDC_ENABLED`). See [Configuration file vs. environment variables](configuration.md#configuration-file-vs-environment-variables) for details.

### Built-in Providers

Gramps Web has built-in support for popular identity providers. To use them, you only need to provide the client ID and client secret:

- **Google**: `OIDC_GOOGLE_CLIENT_ID` and `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` and `OIDC_MICROSOFT_CLIENT_SECRET`

You can configure multiple providers simultaneously. The system will automatically detect which providers are available based on the configuration values.

!!! tip "Microsoft: single-tenant deployments"
    The built-in Microsoft provider uses the multi-tenant `/common` endpoint and accepts logins from any Microsoft account by design. If you only want to allow users from your own tenant, use the [custom OIDC provider](#custom-oidc-providers) with your tenant-specific issuer URL instead, which keeps issuer validation active and restricts logins to that tenant.

### Custom OIDC Providers

For custom OIDC providers (like Keycloak, Authentik, Authelia, or a single-tenant Microsoft Entra tenant), use these settings:

Key | Description
----|-------------
`OIDC_ENABLED` | Boolean, whether to enable OIDC authentication. Set to `True`.
`OIDC_ISSUER` | Your provider's issuer URL. Discovery is fetched from `<issuer>/.well-known/openid-configuration`.
`OIDC_CLIENT_ID` | Client ID for your OIDC provider
`OIDC_CLIENT_SECRET` | Client secret for your OIDC provider
`OIDC_NAME` | Custom display name (optional, defaults to "OIDC")
`OIDC_SCOPES` | OAuth scopes (optional, defaults to "openid email profile")
`OIDC_USERNAME_CLAIM` | Claim used to generate the username (optional, defaults to "preferred_username")
`OIDC_PKCE` | Whether to use PKCE, see [PKCE](#pkce) (optional, enabled automatically if the provider supports it)

### PKCE

Since Gramps Web API 3.23, Gramps Web supports [PKCE](https://datatracker.ietf.org/doc/html/rfc7636) (Proof Key for Code Exchange, `S256` method) for the authorization code flow. Some identity providers, such as Pocket ID, can be configured to *require* PKCE for a client, and refuse logins that don't use it. Older versions of Gramps Web API never use PKCE, so logins with such a client fail.

Whether PKCE is used is decided at login as follows:

- If `OIDC_PKCE` is set to `True`, PKCE is used.
- If `OIDC_PKCE` is set to `False`, PKCE is not used, even if the provider supports it.
- If `OIDC_PKCE` is not set, or set but empty, PKCE is used if the provider's discovery document (`/.well-known/openid-configuration`) lists `S256` in `code_challenge_methods_supported`, and not used otherwise.

For most setups you don't need to set anything. Set `OIDC_PKCE` to `True` if your provider requires PKCE but doesn't advertise `S256` in its discovery document, and to `False` if your provider advertises `S256` but mishandles it. As environment variables, booleans must be lowercase (`GRAMPSWEB_OIDC_PKCE=true`), see [Configuration](configuration.md).

For the built-in providers, the corresponding options are `OIDC_GOOGLE_PKCE` and `OIDC_MICROSOFT_PKCE`.

The PKCE code verifier is kept in the user's session between the redirect to the provider and the callback, so this requires no change to the redirect URIs.

### Multi-Tree Setups

On a multi-tree server, the tree the user is logging into has to be known before Gramps Web redirects to the identity provider, so login starts with:

```
GET /api/oidc/login/?provider=<id>&tree=<tree_id>
```

`tree` is required in multi-tree setups; omitting it, or passing the ID of a tree that doesn't exist, fails the login. On a single-tree server `tree` is optional, but if given it must match the configured `TREE`.

An OIDC identity is bound to exactly one Gramps Web account, which in turn belongs to exactly one tree – logging in against a different tree fails rather than moving the account. There is no way to link a single identity at the provider to accounts in several trees; users who need access to multiple trees need separate identities at the provider (e.g. distinct usernames or accounts).

!!! warning
    A site administrator account with no associated tree (see [creating an admin account](../administration/owner.md)) cannot log in via OIDC, since OIDC login always requires a tree. Such accounts must be created and authenticated with a local username/password instead.

## Required Redirect URIs

When configuring your OIDC provider, you must register the following redirect URI:

**For OIDC providers that support wildcards: (e.g., Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Where `*` is a regex wildcard. Depending on your provider's regex interpreter this could also be a `.*` or similar.
Ensure that regex is enabled if your provider requires it (e.g., Authentik).

**For OIDC providers that do not support wildcards: (e.g., Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/custom`

The tree is never part of the redirect URI, even on multi-tree servers – it travels separately in the session, since providers require the redirect URI to match the registered one exactly.

## Role Mapping

Gramps Web can automatically map OIDC groups or roles from your identity provider to Gramps Web user roles. This allows you to manage user permissions centrally in your identity provider. Role mapping works the same way for all providers, built-in or custom.

### Configuration

Use these settings to configure role mapping:

Key | Description
----|-------------
`OIDC_ROLE_CLAIM` | The claim name in the OIDC token that contains the user's groups/roles. Defaults to "groups". Dotted paths are supported, e.g. `realm_access.roles`.
`OIDC_GROUP_ADMIN` | The group/role name from your OIDC provider that maps to the Gramps "Admin" role
`OIDC_GROUP_OWNER` | The group/role name from your OIDC provider that maps to the Gramps "Owner" role
`OIDC_GROUP_EDITOR` | The group/role name from your OIDC provider that maps to the Gramps "Editor" role
`OIDC_GROUP_CONTRIBUTOR` | The group/role name from your OIDC provider that maps to the Gramps "Contributor" role
`OIDC_GROUP_MEMBER` | The group/role name from your OIDC provider that maps to the Gramps "Member" role
`OIDC_GROUP_GUEST` | The group/role name from your OIDC provider that maps to the Gramps "Guest" role

### Role Mapping Behavior

If no `OIDC_GROUP_*` setting is configured at all, role mapping is off and roles are managed manually in Gramps Web; new OIDC accounts are then created disabled and need to be approved by an existing owner or admin (see [First Login and Bootstrapping](#first-login-and-bootstrapping) below).

Once role mapping is configured, on every login:

- If the role claim is present and the user belongs to a mapped group, they get the corresponding role.
- If the role claim is present but the user belongs to no mapped group, their role is set to disabled. This is a fail-closed default, not a bug – Gramps Web cannot infer a role for a group it doesn't recognize.
- If the role claim is absent from the token entirely, the existing role is left unchanged; a new account still defaults to disabled.

!!! warning "Google does not send a groups claim"
    Google's tokens never include a `groups` claim, so with role mapping enabled, Google logins fall under "claim absent" above: existing users keep their role, but new Google users are created disabled and need manual approval. Keep this in mind before enabling role mapping only for another provider – it does not, by itself, disable existing Google users.

Microsoft Entra returns app roles and group memberships only in the ID token, not from the userinfo endpoint. Gramps Web merges the ID token's claims into the userinfo response so that `OIDC_ROLE_CLAIM` works the same way as for other providers; where both contain a claim, the userinfo value takes precedence.

## First Login and Bootstrapping

New accounts created through OIDC start out disabled unless role mapping assigns them a role (see above). On a brand-new instance nobody can approve a disabled account, and if `OIDC_DISABLE_LOCAL_AUTH` is also enabled there is no password login to fall back on either.

!!! warning "Configure an owner/admin group before the first login"
    Before anyone logs in via OIDC for the first time, set `OIDC_GROUP_OWNER` (or `OIDC_GROUP_ADMIN`) and make sure the first user belongs to that group at the provider. Otherwise the instance cannot be bootstrapped through OIDC at all.

## Accounts and Usernames

Accounts created through OIDC get a generated username, assigned once at account creation and never changed on later logins:

- Built-in providers: `<provider>_<claim value>`, e.g. `microsoft_alice@contoso.com`
- Custom provider: the bare claim value, e.g. `alice`

A numeric suffix is appended on collision. There is no way to rename an OIDC-created account's username afterwards; the full name and e-mail address, by contrast, are refreshed on every login.

An OIDC login never attaches itself to an existing local account that happens to share its e-mail address – this is deliberate, since linking accounts by e-mail is an account-takeover vector. A user who already has a local account gets a second, separate account the first time they log in via OIDC.

E-mail addresses from the provider are only stored if the provider marks them verified (or omits the `email_verified` claim entirely); otherwise the login proceeds without storing an e-mail address. Since e-mail addresses do not have to be unique (since Gramps Web API 3.22), an address is stored even if another account already uses it.

## OIDC Logout

Gramps Web supports Single Sign-Out (SSO logout) for OIDC providers. `GET /api/oidc/logout/` looks up the provider's `end_session_endpoint` and returns it as `logout_url` in the response; it is the Gramps Web frontend that navigates the browser there to actually end the session at the identity provider. `logout_url` is `null` when the provider has no `end_session_endpoint`.

!!! warning "Tokens are not revoked on logout"
    Logging out only ends the browser session; there is currently no way to revoke a Gramps Web token that has already been issued. Tokens stay valid until they expire (`JWT_ACCESS_TOKEN_EXPIRES`, default 15 minutes for access tokens), regardless of whether the user has since logged out at Gramps Web or at the identity provider.

## Troubleshooting

Start at the point where login stops and follow the branch. Gramps Web logs the reason for a failed callback (look for `OIDC callback error for provider` in the server log), which is usually more specific than the message shown in the browser.

**1. Is the login button missing?**

- Check `<BASE_URL>/api/oidc/config/`. If `enabled` is `false` or `providers` is empty, OIDC is not configured: `OIDC_ENABLED` must be `True`, and a custom provider needs both `OIDC_ISSUER` and `OIDC_CLIENT_ID`.
- A built-in provider (Google, Microsoft) is only registered if both its client ID and its client secret are set.
- Look in the server log at startup for `Could not load discovery document`. This means the server could not reach `<issuer>/.well-known/openid-configuration` (or `OIDC_OPENID_CONFIG_URL`). It retries on first use, but the Gramps Web container must be able to resolve and reach the issuer URL itself, not just your browser.

**2. Does the browser get an error right after being sent to the provider?**

The error is shown by the identity provider, before you log in.

- *"redirect URI mismatch"* (or similar): the redirect URI registered at the provider must match exactly, including scheme, host, port and provider ID. See [Required Redirect URIs](#required-redirect-uris). Note that it is built from `BASE_URL`, so a wrong `BASE_URL` gives a wrong redirect URI.
- *A PKCE error* (for example `invalid_request`, "code challenge required", or a missing `code_challenge` parameter): the provider requires PKCE but Gramps Web did not send it. Go to [the PKCE branch](#pkce-branch) below.

**3. Does the provider accept the login but Gramps Web then shows an error?**

- *`mismatching_state`, or the error mentions the session or state*: the browser did not send back the session cookie that Gramps Web set when the login started. This cookie also carries the PKCE code verifier. Make sure that the address in the browser matches `BASE_URL` (same scheme and host), that a reverse proxy passes cookies and the original host through, and that the login is started and completed in the same browser tab or window.
- *`OIDC authentication failed for <provider>` (HTTP 401)*: check the server log for the underlying reason. Common causes are a wrong client secret, an issuer URL that does not match the `iss` claim of the tokens, and the provider returning an error to the callback (for example PKCE, see below).
- *Too many attempts*: the login and callback endpoints are rate limited (5 requests per minute). Wait a minute and retry.

**4. Does login succeed but you see "Account Under Review", or can't do anything?**

New accounts are created disabled unless role mapping assigns a role. See [First Login and Bootstrapping](#first-login-and-bootstrapping) and [Role Mapping Behavior](#role-mapping-behavior). An administrator can also activate the account under Settings > Administration > Manage users.

### PKCE branch

Gramps Web decides whether to use PKCE when a login starts (see [PKCE](#pkce)). To find out what happened for your setup, work through these questions in order:

1. **Is `OIDC_PKCE` set?** (For built-in providers, `OIDC_GOOGLE_PKCE` or `OIDC_MICROSOFT_PKCE`.)
    - `True`: PKCE is used. Skip to question 3.
    - `False`: PKCE is deliberately off, and the provider's discovery document is ignored. If your provider requires PKCE, remove the setting or set it to `True`.
    - Not set, or empty: continue with question 2.
2. **Does the discovery document list `S256`?** Open `<issuer>/.well-known/openid-configuration` and look for `S256` in `code_challenge_methods_supported`.
    - Yes: PKCE is used automatically. Continue with question 3.
    - No, or the field is missing: PKCE is **not** used. Set `OIDC_PKCE` to `True` if your provider requires it. Also check the server log for `Could not check the provider for PKCE support`, which means the discovery document could not be fetched and PKCE was therefore left off.
3. **Was PKCE really sent?** Start a login and look at the address of the provider's login page (or the first redirect in your browser's network tab). It should contain `code_challenge=` and `code_challenge_method=S256`.
    - Present, but the login still fails at the callback: the provider rejected the code verifier. The session cookie may have been lost between the redirect and the callback (see branch 3 above), or the provider does not support `S256`, in which case set `OIDC_PKCE` to `False` if the provider does not require PKCE.
    - Absent: the settings above were not applied. Check that the environment variable has the right prefix and a lowercase value (for example `GRAMPSWEB_OIDC_PKCE=true` in Docker; `True` is not read as a boolean), restart the server, and look at the configuration again.

!!! note
    With PKCE enabled at the provider as *optional*, or not enabled at all, logins work whether or not Gramps Web sends a challenge. Only providers (or clients) configured to *require* PKCE make this setting matter.

## Example Configurations

### Custom OIDC Provider (Keycloak)

```python
TREE="My Family Tree"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # your secret key
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Custom OIDC Configuration
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.example.com/realms/myrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="your-client-secret"
OIDC_NAME="Family SSO"
OIDC_SCOPES="openid email profile"
OIDC_AUTO_REDIRECT=True  # Optional: automatically redirect to SSO login
OIDC_DISABLE_LOCAL_AUTH=True  # Optional: disable username/password login

# Optional: Role mapping from OIDC groups to Gramps roles
OIDC_ROLE_CLAIM="groups"  # or "roles" depending on your provider
OIDC_GROUP_ADMIN="gramps-admins"
OIDC_GROUP_EDITOR="gramps-editors"
OIDC_GROUP_MEMBER="gramps-members"

EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # Use implicit SSL for port 465
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # your SMTP password
DEFAULT_FROM_EMAIL="gramps@example.com"
```

### Built-in Provider (Google)

```python
TREE="My Family Tree"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # your secret key
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="your-google-client-id"
OIDC_GOOGLE_CLIENT_SECRET="your-google-client-secret"
```

### Multiple Providers

You can enable multiple OIDC providers simultaneously:

```python
TREE="My Family Tree"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # your secret key
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Custom provider
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.example.com/realms/myrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="your-client-secret"
OIDC_NAME="Company SSO"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="your-google-client-id"
OIDC_GOOGLE_CLIENT_SECRET="your-google-client-secret"

# Microsoft OAuth
OIDC_MICROSOFT_CLIENT_ID="your-microsoft-client-id"
OIDC_MICROSOFT_CLIENT_SECRET="your-microsoft-client-secret"
```

### Pocket ID

Create an OIDC client in Pocket ID with the redirect URI `<BASE_URL>/api/oidc/callback/custom` (see [Required Redirect URIs](#required-redirect-uris)). If you enable "Require PKCE" for the client, no additional Gramps Web configuration is needed, since Pocket ID advertises PKCE support in its discovery document. Then configure:

```
GRAMPSWEB_OIDC_ENABLED=True
GRAMPSWEB_OIDC_ISSUER=https://id.example.com
GRAMPSWEB_OIDC_CLIENT_ID=<client id>
GRAMPSWEB_OIDC_CLIENT_SECRET=<client secret>
GRAMPSWEB_OIDC_NAME=Pocket ID
```

### Authelia

A community-made OIDC setup guide for Gramps Web is available on the [official Authelia documentation website](https://www.authelia.com/integration/openid-connect/clients/gramps/).

### Keycloak

Most of the configuration for Keycloak can be left at its defaults (*Client → Create client → Client authentication ON*).
There are a few exceptions:

1. **OpenID scope** – The `openid` scope isn't included by default in all Keycloak versions. To avoid issues, add it manually: *Client → [Gramps client] → Client scopes → Add scope → Name: `openid` → Set as default.*
2. **Roles** – Roles can be assigned either at the client level or globally per realm.

    * If you're using client roles, set the `OIDC_ROLE_CLAIM` config option to: `resource_access.[gramps-client-name].roles`
    * To make roles visible to Gramps, navigate to *Client Scopes* (the top‑level section, not under the specific client), then: *Roles → Mappers → client roles → Add to userinfo → ON.*
