# User Settings

User Settings are accessible via the user icon in the top app bar, then **User Settings**. The page is organized into collapsible sections. Changes take effect immediately unless noted otherwise.

!!! note
    Changes in User Settings only affect your own account. Settings that affect all users of the tree are managed in [Administration Settings](../administration/settings.md).

## Account

Covers your profile information, credentials, and account security.

### User information

Shows your **username** and current **user role** (e.g. Guest, Member, Editor). These are read-only.

### Change e-mail

Enter a new e-mail address and click **Submit** to update the address associated with your account. The e-mail address is used for password resets and (if configured) notifications.

### Change password

Enter your current password and a new password, then click **Submit**. If you have forgotten your current password, use the **Forgot password** link on the login page instead.

### Linked sign-in methods

If your server offers single sign-on (see [OIDC authentication](../install_setup/oidc.md)), you can link an account from a provider, such as Google or your organization's login, to your Gramps Web account. You can then sign in with that provider and land in your existing account, with your role and your edits. This section only appears when single sign-on is enabled and the server supports linking (Gramps Web API 3.24 and later).

To link an account, click **Link with** and the provider's name, sign in at the provider, and you are taken back to your settings. If you haven't signed in recently, you are asked to sign in again first.

A provider account can only be linked to one Gramps Web account. If you see "This sign-in is already linked to another account", it is linked elsewhere, for example to an account that was created when you first signed in with that provider. An administrator can delete that other account, after which you can link it to yours.

To unlink an account, click **Unlink**. If it is your last linked sign-in method, you also need to enter your password, so that you can still sign in afterwards. If your account was created through single sign-on and you never set a password, use **Forgot password** on the login page to set one first (this needs the server to send e-mails). If the server only allows signing in through a provider, the last linked account can't be unlinked.

## Appearance

Controls display preferences saved on your device.

### Language

Select the language for the Gramps Web interface. The language setting is stored in the browser's local storage and applies only to the current device.

### Theme

Choose between:

- **System** – follows the operating system's light/dark preference (default)
- **Light** – always use the light theme
- **Dark** – always use the dark theme

The theme setting is stored in the browser's local storage.

### Family tree preferences

#### Default family tree view

Sets which chart type opens by default when you navigate to the [Family Tree](tree.md) page. Options are Ancestor Tree, Descendant Tree, Hourglass Graph, Relationship Graph, and Fan Chart.

This preference is stored in the browser's local storage.

## Developer tools

### API token

Copies your current session token to the clipboard. The token can be used to authenticate directly against the REST API, for example in the interactive Swagger UI served by your Gramps Web instance at `/api/swagger-ui`.

Click **Launch Swagger** to open the Swagger UI in a new tab with your session already available.

!!! note
    The session token is short-lived. Copy it immediately before using it in Swagger, as it may expire.
