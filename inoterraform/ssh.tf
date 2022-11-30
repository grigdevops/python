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
    private_key = "/grigscript"
    timeout = "60s"

    user = "root"

    port  = 22

    commands = ["pwd"]



}