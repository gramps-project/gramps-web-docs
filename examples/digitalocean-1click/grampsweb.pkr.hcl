packer {
  required_plugins {
    digitalocean = {
      version = ">= 1.4.2"
      source  = "github.com/digitalocean/digitalocean"
    }
  }
}

variable "do_token" {
  type      = string
  default   = env("DIGITALOCEAN_TOKEN")
  sensitive = true
}

variable "apt_packages" {
  type    = string
  default = "software-properties-common apt-transport-https ca-certificates openssl ufw curl"
}

locals {
  image_name = "grampsweb-marketplace-${formatdate("YYYYMMDDhhmmss", timestamp())}"
  # same environment for all shell provisioners
  shell_env = [
    "DEBIAN_FRONTEND=noninteractive",
    "LC_ALL=C",
    "LANG=en_US.UTF-8",
    "LC_CTYPE=en_US.UTF-8",
  ]
}

source "digitalocean" "grampsweb" {
  api_token     = var.do_token
  image         = "ubuntu-26-04-x64"
  region        = "fra1"
  size          = "s-1vcpu-1gb"
  ssh_username  = "root"
  snapshot_name = local.image_name
}

build {
  sources = ["source.digitalocean.grampsweb"]

  provisioner "shell" {
    inline = [
      "cloud-init status --wait",
      "mkdir /opt/grampsweb",
    ]
  }

  provisioner "file" {
    sources = [
      "docker-compose.yml",
      "nginx_proxy.conf",
      "firstlogin.sh",
      "firstlogin.py",
    ]
    destination = "/opt/grampsweb/"
  }

  provisioner "shell" {
    environment_vars = local.shell_env
    inline = [
      "echo 'Acquire::Retries \"10\";' > /etc/apt/apt.conf.d/80retry",
      "echo 'APT::Install-Recommends \"false\";' > /etc/apt/apt.conf.d/80recommends",
      "echo 'APT::Install-Suggests \"false\";' > /etc/apt/apt.conf.d/80suggests",
      "echo 'APT::Get::Assume-Yes \"true\";' > /etc/apt/apt.conf.d/80forceyes",
      "echo 'APT::Get::Fix-Missing \"true\";' > /etc/apt/apt.conf.d/80fixmissing",
      "apt-get -qq update",
      "apt-get -qq -o Dpkg::Options::='--force-confdef' -o Dpkg::Options::='--force-confold' full-upgrade",
      "apt-get -qq install ${var.apt_packages}",
      "chmod 700 /opt/grampsweb/firstlogin.py",
      "chmod 700 /opt/grampsweb/firstlogin.sh",
    ]
  }

  provisioner "shell" {
    environment_vars = local.shell_env
    scripts = [
      "install_grampsweb.sh",
      "scripts/firewall.sh",
      "scripts/cleanup.sh",
      "scripts/check.sh",
    ]
  }
}
