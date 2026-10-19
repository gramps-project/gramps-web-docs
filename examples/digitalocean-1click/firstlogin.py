#!/usr/bin/env python3

"""Gramps 1-click app first run script."""

import getpass
import os


def env_value(value):
    """Quote a value for a Docker Compose env file, so it is read literally."""
    if "'" not in value:
        # single quotes: no interpolation, no escapes
        return f"'{value}'"
    escaped = value.replace("\\", "\\\\").replace('"', '\\"').replace("$", "$$")
    return f'"{escaped}"'


def ask_email_settings():
    """Ask for the optional SMTP settings; return them as environment lines."""
    print(
        "\nOptionally, enter the SMTP settings Gramps Web will use to send"
        " e-mails, e.g. for password resets. Leave the host empty to skip;"
        " you can add them later, see the documentation."
    )
    host = input("SMTP host:\n").strip()
    if not host:
        return ""
    port = input("SMTP port [465]:\n").strip() or "465"
    user = input("SMTP user:\n").strip()
    password = getpass.getpass("SMTP password:\n")
    from_email = input("From address:\n").strip()
    # port 465 uses implicit SSL, other ports STARTTLS
    use_ssl = "true" if port == "465" else "false"
    use_starttls = "false" if port == "465" else "true"
    return f"""GRAMPSWEB_EMAIL_HOST={host}
GRAMPSWEB_EMAIL_PORT={port}
GRAMPSWEB_EMAIL_HOST_USER={env_value(user)}
GRAMPSWEB_EMAIL_HOST_PASSWORD={env_value(password)}
GRAMPSWEB_DEFAULT_FROM_EMAIL={env_value(from_email)}
GRAMPSWEB_EMAIL_USE_SSL={use_ssl}
GRAMPSWEB_EMAIL_USE_STARTTLS={use_starttls}
"""


def firstrun():
    """First run script."""

    print("Welcome to the Gramps Web DigitalOcean 1-click app setup!\n")
    while True:
        host = input("Please enter the domain name you will use for Gramps Web:\n")
        # remove URL scheme if present
        host = host.split("://")[-1].rstrip("/")
        if host:
            break
        print("The domain name is mandatory.")
    email = input(
        "Optionally, please enter the e-mail address"
        " that will be associated with your Let's Encrypt certificate:\n"
    )

    dotenv = f"""VIRTUAL_HOST={host}
LETSENCRYPT_HOST={host}
LETSENCRYPT_EMAIL={email}
GRAMPSWEB_BASE_URL=https://{host}
"""
    dotenv += ask_email_settings()
    # may hold the SMTP password
    fd = os.open("letsencrypt.env", os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    os.fchmod(fd, 0o600)
    with open(fd, "w", encoding="utf-8") as f:
        f.write(dotenv)


if __name__ == "__main__":
    firstrun()
