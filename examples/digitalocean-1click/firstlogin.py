#!/usr/bin/env python3

"""Gramps 1-click app first run script."""


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
"""
    with open("letsencrypt.env", "w", encoding="utf-8") as f:
        f.write(dotenv)


if __name__ == "__main__":
    firstrun()
