
# Getting started with Gramps Web

Gramps Web is a web app that runs on a server and is accessed via the web browser. It is meant to be made accessible to authenticated users via the internet.

If you want to use Gramps Web for your genealogical research data, you have to choose one of the following options:

1. Self-host on your own hardware
2. Self-host in the cloud
3. Sign up for a hosted instance

While the first option gives you maximal flexibility and control, it can also be technically challenging.

!!! tip
    One of the main principles of Gramps Web is to put users in control of their own data at any time, so migrating data from one instance to another is simple. Don't worry about being locked in after having chosen one of the options!

## Self-host on your own hardware

The most convenient way to host Gramps Web is via Docker Compose. We also provide Docker images for the ARM architecture, so you can run Gramps Web on a Raspberry Pi in your basement.

See [Deploy with Docker](Deployment.md) for setup instructions.


## Self-host in the cloud

Installing Gramps Web can be more challenging than other, simple web applications and is not compatible with ordinary "shared hosting" providers. You can sign up for a virtual server and install Gramps Web [manually](Deployment.md).

A simpler option is to use a pre-installed cloud image. One example is our [DigitalOcean 1-click app](DigitalOcean.md).

## Sign up for a hosted instance

Features to manage a server hosting multiple, securely separated instances of Gramps Web have been added recently. We expected hosted Gramps Web will be available soon. Stay tuned!