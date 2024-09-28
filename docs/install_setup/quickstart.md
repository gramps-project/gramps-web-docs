To try out Gramps Web on your local computer (Linux, Mac, or Windows) without interfering with your Gramps Desktop installation, you can use Docker with the following command:

```bash
docker run -p "5055:5000" -e TREE=new ghcr.io/gramps-project/grampsweb:latest
```

This will make a new, empty Gramps Web instance accessible at [http://localhost:5055](http://localhost:5055), where you can create an admin user and import a Gramps XML file.

!!! info
    Since this simple setup does not allow running long tasks in a separate process, importing a large Gramps XML file might fail due to a timeout in the first-run assistant.


To use media files from your computer you can mount the Gramps media folder into the container with

```bash
docker run -p "5055:5000" -e TREE=new \
  -v /path/to/my/gramps_media_folder:/app/media \
  ghcr.io/gramps-project/grampsweb:latest
```

Note that this will not persist the changes you make to the database when you restart the container. To properly set up Gramps Web, continue reading about [Deployment](install_setup/deployment.md).