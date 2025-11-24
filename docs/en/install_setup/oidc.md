# OIDC Authentication

Gramps Web supports OpenID Connect (OIDC) authentication, allowing users to log in using external identity providers. This includes both popular providers like Google, Microsoft, and GitHub, as well as custom OIDC providers like Keycloak, Authentik, and others.

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
- **GitHub**: `OIDC_GITHUB_CLIENT_ID` and `OIDC_GITHUB_CLIENT_SECRET`

You can configure multiple providers simultaneously. The system will automatically detect which providers are available based on the configuration values.

### Custom OIDC Providers

For custom OIDC providers (like Keycloak, Authentik, or any standard OIDC-compliant provider), use these settings:

Key | Description
----|-------------
`OIDC_ENABLED` | Boolean, whether to enable OIDC authentication. Set to `True`.
`OIDC_ISSUER` | Your provider's issuer URL
`OIDC_CLIENT_ID` | Client ID for your OIDC provider
`OIDC_CLIENT_SECRET` | Client secret for your OIDC provider
`OIDC_NAME` | Custom display name (optional, defaults to "OIDC")
`OIDC_SCOPES` | OAuth scopes (optional, defaults to "openid email profile")

## Required Redirect URIs

When configuring your OIDC provider, you must register the following redirect URI:

**For OIDC providers that support wildcards: (e.g., Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Where `*` is a regex wildcard. Depending on your provider's regex interpreter this could also be a `.*` or similar.
Ensure that regex is enabled if your provider requires it (e.g., Authentik).

**For OIDC providers that do not support wildcards: (e.g., Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/?provider=custom`

## Role Mapping

Gramps Web can automatically map OIDC groups or roles from your identity provider to Gramps Web user roles. This allows you to manage user permissions centrally in your identity provider.

### Configuration

Use these settings to configure role mapping:

Key | Description
----|-------------
`OIDC_ROLE_CLAIM` | The claim name in the OIDC token that contains the user's groups/roles. Defaults to "groups"
`OIDC_GROUP_ADMIN` | The group/role name from your OIDC provider that maps to the Gramps "Admin" role
`OIDC_GROUP_OWNER` | The group/role name from your OIDC provider that maps to the Gramps "Owner" role
`OIDC_GROUP_EDITOR` | The group/role name from your OIDC provider that maps to the Gramps "Editor" role
`OIDC_GROUP_CONTRIBUTOR` | The group/role name from your OIDC provider that maps to the Gramps "Contributor" role
`OIDC_GROUP_MEMBER` | The group/role name from your OIDC provider that maps to the Gramps "Member" role
`OIDC_GROUP_GUEST` | The group/role name from your OIDC provider that maps to the Gramps "Guest" role

### Role Mapping Behavior

- If no role mapping is configured (no `OIDC_GROUP_*` variables set), existing user roles are preserved
- Users are assigned the highest role they are entitled to based on their group membership
- Role mapping is case-sensitive by default (depends on your OIDC provider)

## OIDC Logout

Gramps Web supports Single Sign-Out (SSO logout) for OIDC providers. When a user logs out from Gramps Web after authenticating via OIDC, they will be automatically redirected to the identity provider's logout page if the provider supports the `end_session_endpoint`.

### Backchannel Logout

Gramps Web implements the OpenID Connect Back-Channel Logout specification. This allows identity providers to notify Gramps Web when a user logs out from another application or the identity provider itself.

#### Configuration

To configure backchannel logout with your identity provider:

1. **Register the backchannel logout endpoint** in your identity provider's client configuration:
   ```
   https://your-gramps-backend.com/api/oidc/backchannel-logout/
   ```

2. **Configure your provider** to send logout notifications. The exact steps depend on your provider:

   **Keycloak:**

   - In your client configuration, navigate to "Settings"
   - Set "Backchannel Logout URL" to `https://your-gramps-backend.com/api/oidc/backchannel-logout/`
   - Enable "Backchannel Logout Session Required" if you want session-based logout

   **Authentik:**

   - In your provider configuration, add the backchannel logout URL
   - Ensure the provider is configured to send logout tokens

!!! warning "Token Expiration"
    Due to the stateless nature of JWT tokens, backchannel logout currently logs the logout event but cannot immediately revoke already-issued JWT tokens. Tokens will remain valid until they expire (default: 15 minutes for access tokens).

    For enhanced security, consider:

    - Reducing JWT token expiration time (`JWT_ACCESS_TOKEN_EXPIRES`)
    - Educating users to manually log out from Gramps Web when logging out from your identity provider

!!! tip "How It Works"
    When a user logs out from your identity provider or another application:

    1. The provider sends a `logout_token` JWT to Gramps Web's backchannel logout endpoint
    2. Gramps Web validates the token and logs the logout event
    3. The logout token's JTI is added to a blocklist to prevent replay attacks
    4. Any new API requests with the user's JWT will be denied once tokens expire

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
EMAIL_USE_TLS=True
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

# GitHub OAuth
OIDC_GITHUB_CLIENT_ID="your-github-client-id"
OIDC_GITHUB_CLIENT_SECRET="your-github-client-secret"
```

### Authelia

A community-made OIDC setup guide for Gramps Web is available on the [official Authelia documentation website](https://www.authelia.com/integration/openid-connect/clients/gramps/).
