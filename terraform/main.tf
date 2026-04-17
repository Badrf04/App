terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

# Référence à l'image construite par Jenkins
resource "docker_image" "app_image" {
  name         = "mon-app-cyber:latest"
  keep_locally = true
}

# Déploiement du conteneur
resource "docker_container" "app_container" {
  name  = "openrecon-service"
  image = docker_image.app_image.image_id
  
  # Redirection du port : 8081 (Public) -> 5000 (Privé NiceGUI)
  ports {
    internal = 5000
    external = 8081
  }

  # Options de cycle de vie pour l'automatisation
  must_run = true
  restart  = "always"
}
