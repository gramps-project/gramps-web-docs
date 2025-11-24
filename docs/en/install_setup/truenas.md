# TrueNAS Setup

This guide explains how to set up Gramps Web on TrueNAS Community Edition 25.04.

!!! warning
    This guide is intended for TrueNAS Community Edition 25.04 or later, which introduced a new Docker Compose-based apps system. It does not apply to earlier versions of TrueNAS.

## Prerequisites

- TrueNAS Community Edition 25.04 or later
- Basic familiarity with TrueNAS web interface
- A dataset for storing Gramps Web data

## Overview

TrueNAS Community Edition 25.04 introduced a new Docker Compose-based apps system that replaces the previous Helm chart-based approach. This guide will walk you through creating a custom app for Gramps Web using Docker Compose.

## Step 1: Prepare Storage

1. Navigate to **Datasets** in the TrueNAS web interface
2. Create a new dataset for Gramps Web (e.g., `grampsweb`). Note the full path to this dataset, e.g., `/mnt/storage/grampsweb`, as you will need it later.

Create subdirectories for the various components:
- `users` - User database
- `database` - Gramps database file(s)
- `media` - Media files



## Step 2: Create the Docker Compose App

1. Navigate to **Apps** in the TrueNAS web interface
2. Click on **Discover Apps**
3. Search for "Gramps Web" and click on it
4. Click "Install"

This will take you to a the app configuration page.

## Step 3: Configure the App

### Gramps Web configuration

- **Timezone:** Set to your local timezone (e.g., `Europe/Berlin`)
- **Redis password:** Set a password for Redis. This will only be used internally by the app.
- **Disable telemetry:** please leave this box unchecked – see [here for details](telemetry.md).
- **Secret key:** it is crucial that you set this to a strong, unique value. See [server configuration](configuration.md#existing-configuration-settings) for instructions how to generate a random key.
- **Additional Environment Variables:** You will need to set all additional [configuration options](configuration.md) as environment variables prefixed by `GRAMPSWEB_`. Please check the [configuration documentation](configuration.md) in detail – for instance the fact that boolean values need to be set as `true` or `false` (all lowercase) in the case of environment variables, a common pitfall.

Please **at least** set the `GRAMPSWEB_BASE_URL` to the URL your Gramps Web instance will be accessible at – this is required for proper operation.

You might also want to set up email configuration at this stage. If you do, you can skip the email configuration step in the onboarding wizard. The relevant environment variables are:

- `GRAMPSWEB_EMAIL_HOST`
- `GRAMPSWEB_EMAIL_HOST_USER`
- `GRAMPSWEB_EMAIL_HOST_PASSWORD`
- `GRAMPSWEB_DEFAULT_FROM_EMAIL`

All configuration settings can be changed later by clicking "Edit" in the TrueNAS Apps interface.


### Storage Configuration

- **Users Storage**: Select the path to the `users` directory you created earlier.
- **Index Storage**: You can leave the default setting "ixVolume (Dataset created automatically by the system)"
- **Thumbnail Cache Storage**: You can leave the default setting "ixVolume (Dataset created automatically by the system)"
- **Cache Storage**: You can leave the default setting "ixVolume (Dataset created automatically by the system)"
- **Media Storage**: Select the path to the `media` directory you created earlier.
- **Gramps Database Storage**: Select the path to the `database` directory you created earlier.

### Resources Configuration

We recommend you allocate at least 2 CPUs and 4096 MB of RAM to ensure smooth operation.


## Step 4: Access Gramps Web

Once the app is deployed, you can access Gramps Web by clicking the "Web UI" button in the TrueNAS Apps interface. You should see the onboarding wizard "Welcome to Gramps Web".

If you want to allow users to access your Gramps Web interface, **do not** expose the app directly to the internet, but proceed to the next step.


## Step 5: Set Up a Reverse Proxy

To securely expose your Gramps Web instance to users, it is recommended to set up a reverse proxy. This allows you to manage SSL/TLS certificates and control access.

The easiest option is to use the official TrueNAS Nginx Proxy Manager app. Search for the app in the TrueNAS Apps interface and install it. You can leave all settings at their defaults, but we recommend you set one additional environment variable: `DISABLE_IPV6` with value `true` to avoid potential IPv6-related issues.

Once deployed, open the Nginx Proxy Manager web interface and create a new proxy host with the following settings:

- Scheme: `http`
- Forward Hostname / IP: the hostname of your TrueNAS server (e.g. `truenas`)
- Forward Port: the port assigned to your Gramps Web app (check the TrueNAS Apps interface for the exact port)
- In the "SSL" tab, check "Force SSL"
- Under   "SSL Certificates", select "Add SSL Certificate" > "Let's Encrypt" to create a new Let's Encrypt certificate for your domain.

Please see the [Nginx Proxy Manager documentation](https://nginxproxymanager.com/guide/) for more details on configuring your router and obtaining SSL certificates.