# Setup Requirements

Gramps Web is a web app that runs on a server and is accessed via the web browser. It is meant to be made accessible to authenticated users via the internet.

## Server Requirements

The most convenient way to host Gramps Web is via Docker Compose. While this is not possible with ordinary "shared hosting" providers, this makes it possible to host the app on Linux, Mac, or Windows; it can be hosted on a virtual server or on a Raspberry Pi (we provide Docker images for the ARM architecture) in your basement.

Apart from Docker, you will also need some storage space to store your media files (images, documents).

Finally, Gramps Web is only secure when served via HTTPS, so you will require an SSL/TLS certificate. The docs below show how to get one automatically for free from Let's Encrypt.
