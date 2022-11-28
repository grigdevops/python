terraform {
  required_providers {
    ssh = {
        source = "loafoe/ssh"
        version = "2.3.0"
    }
  }
}

provider "ssh" {
  # Configuration options
}


resource "ssh_resource" "inossh" {
    host = "95.111.230.51"

    user = "root"

    port  = 22

    commands = ["wget"]



}