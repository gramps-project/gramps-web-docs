# Gramps Web DigitalOcean 1-click app

This directory contains the scripts to build a snapshot for the [Gramps Web DigitalOcean 1-click app](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy).

To build, set the `DIGITALOCEAN_TOKEN` environment variable to a DigitalOcean API token and run

```bash
packer init grampsweb.pkr.hcl
packer build grampsweb.pkr.hcl
```

`scripts/check.sh` and `scripts/cleanup.sh` are based on the scripts in [https://github.com/digitalocean/marketplace-partners](https://github.com/digitalocean/marketplace-partners), which also has general instructions.
