# User Settings

User Settings are accessible via the user icon in the top app bar, then **User Settings**. Changes take effect immediately unless noted otherwise.

## User information

Shows your **username** and current **user role** (e.g. Guest, Member, Editor). These are read-only.

## Language

Select the language for the Gramps Web interface. The language setting is stored in the browser's local storage and applies only to the current device.

## Theme

Choose between:

- **System** – follows the operating system's light/dark preference (default)
- **Light** – always use the light theme
- **Dark** – always use the dark theme

The theme setting is stored in the browser's local storage.

## Change e-mail

Enter a new e-mail address and click **Submit** to update the address associated with your account. The e-mail address is used for password resets and (if configured) notifications.

## Change password

Enter your current password and a new password, then click **Submit**. If you have forgotten your current password, use the **Forgot password** link on the login page instead.

## Family tree preferences

### Default family tree view

Sets which chart type opens by default when you navigate to the [Family Tree](tree.md) page. Options are Ancestor Tree, Descendant Tree, Hourglass Graph, Relationship Graph, and Fan Chart.

This preference is stored in the browser's local storage.

## Developer tools

### API token

Copies your current session token to the clipboard. The token can be used to authenticate directly against the REST API, for example in the interactive Swagger UI served by your Gramps Web instance at `/api/swagger-ui`.

Click **Launch Swagger** to open the Swagger UI in a new tab with your session already available.

!!! note
    The session token is short-lived. Copy it immediately before using it in Swagger, as it may expire.
