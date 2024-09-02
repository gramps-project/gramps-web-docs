# Deploying Gramps Web with Docker

The most convenient option to host Gramps Web on your own server (or virtual server) is with Docker Compose.

We will assume that Docker and Docker Compose are already installed in your system. You can use Windows, Mac OS, or Linux as a host system. The supported architectures include not only x86-64 (desktop systems), but also ARM systems such as a Raspberry Pi, which can serve as a low-cost, but powerful (enough) web server.

!!! note
    You do not need to install Gramps on the server as it is contained in the docker image.


## Step 1: Docker configuration

Create a new file on the server named `docker-compose.yml` and insert the following contents: [docker-compose.yml](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-base/docker-compose.yml).



This will generate six named volumes to make sure that all relevant data will persist when restarting the container.

!!! warning
    The above will make the API available on port 80 of the host machine **without SSL/TLS protection**. You can use this for local testing, but do not expose this directly to the internet, it is completely insecure!

## Step 2: Secure access with SSL/TLS

The web API **must** be served to the public internet over HTTPS. There are several options, e.g.

- Using docker hosting that includes SSL/TLS automatically
- Using an Nginx Reverse Proxy with a Let's Encrypt certificate

See [Docker with Let's Encrypt](LetsEncrypt.md) for how to set up the former.

If you plan to use Gramps Web only on your local network, you can skip this step.

## Step 3: Start the server

Run

```
docker compose up -d
```

On first run, the app will display a first-run wizard that will allow you to

- Create and account for the owner (admin) user
- Set some necessary configuration options
- Import a family tree in Gramps XML (`.gramps`) format

## Step 4: Upload media files

There are several options for uploading media files.

- When using files stored on the same server as Gramps Web, you can mount a directory into the Docker container instead of using a named volume, i.e. `/home/server_user/gramps_media/:/app/media`instead of `gramps_media:/app/media`, and upload your media files there.
- When using media files [hosted on S3](s3.md), you can use he S3 Media Uploader Addon
- The arguably most convenient option is to use [Gramps Web Sync](user-guide/sync.md).
