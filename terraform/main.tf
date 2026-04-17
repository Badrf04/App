terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_image" "app_image" {
  name         = "mon-app-cyber:latest"
  keep_locally = true
}

resource "docker_container" "app_container" {
  name  = "openrecon-service"
  image = docker_image.app_image.name
  restart = "always"

  ports {
    internal = 5000   # LIAISON : Le port de main.py
    external = 8081   # LIAISON : Le port testé par Ansible
    ip       = "0.0.0.0"
  }
}
