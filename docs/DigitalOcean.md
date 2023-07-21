# Gramps Web DigitalOcean 1-Click App

Instead of [setting up Gramps Web yourself](Deployment.md), you can also use the [Gramps Web DigitalOcean 1-Click App](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy).

As part of the setup procedure, you will have to sign up for an account with DigitalOcean and select a paid plan for the "droplet" (virtual machine) to use.

Arguably, this is currently the simplest way to deploy your own, self-hosted Gramps Web instance, secured with SSL, without using your own hardware.

!!! info
    Note that you will be paying DigitalOcean for the hosting services. The Gramps open source project does not provide paid support.

## Step 1: Create a DigitalOcean account

Create an account at [DigitalOcean](https://www.digitalocean.com/) if you don't have one yet.

## Step 2: Create the droplet

- Go to [Gramps Web 1-Click App](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy) and click "Create Gramps Web Droplet".
- Choose a plan with at least 1 GB of RAM.
- Set up authentication to your droplet
- Click "Create Droplet"

## Step 3: Set up a domain name

You will need a domain name (or subdomain). If you own a domain, point it to the IP address of your droplet. Otherwise, you could use a free service such as [DuckDNS](https://www.duckdns.org/).

## Step 4: Log in to your droplet

SSH into your droplet. You should be presented with the message "Welcome to the Gramps Web DigitalOcean 1-click app setup!". If this is not the case, wait a few minutes and try again (the installation is not yet finished).

The setup script will ask you for the domain name (e.g. `mygrampswebinstance.duckdns.org`) and an e-mail address (needed for the Let's Encrypt certificate).

When this is done, wait for the setup to be completed in the background

## Step 5: Launch Gramps Web

Your Gramps Web instance should now be accessible at the root of your domain, with a valid SSL certificate, and it should be showing the first-run assistant.