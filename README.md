# proxmox_management

This Ansible collection makes it easy to provision, configure, and manage Proxmox LXC containers. It includes several roles that handle everything from setting up containers to applying advanced configurations and even deploying Docker containers inside them.

## Overview

The collection is composed of the following roles:

* **proxmox_provision** – Creates and starts LXC containers on a Proxmox host using the Proxmox API.
* **container_inventory** – Retrieves container IP addresses using a Python script and automatically adds them to the Ansible inventory.
* **container_setup** – Handles basic setup, like updating packages, creating non-root users, and disabling root login.
* **container_extras** – Runs additional non-root setup tasks, such as installing extra packages and customizing system messages.
* **docker_compose** – Deploys and manages Docker containers on LXC hosts using Docker Compose.

These roles are designed to work together, starting with container creation and ending with full application deployment via Docker.

## Requirements

To use this collection, you'll need:

* **Ansible:** Version 2.9 or later.
* **Python Libraries (on the control node):**
    - proxmoxer
    - requests
    - passlib
* **Ansible Collection Dependency:** community.general (>=6.0.0)
* **Proxmox API Access:** Valid credentials and network access to your Proxmox server.

_Note:_ I recommend using `geerlingguy.docker` to install Docker and its dependencies.

## Quick Start

1. **Set up your environment:** Use the `bootstrap.yml` playbook in `examples/` to install the required dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install ansible
   ansible-playbook examples/bootstrap.yml
   ```

2. **Install the collection:**

   ```bash
   ansible-galaxy collection install sbarbett.proxmox_management
   ```

3. **Configure your vault and container definitions** in `group_vars/`.

## Usage

You can integrate this collection into your playbooks for a complete workflow. Here are some useful examples:

* [Example playbook: Full LXC workflow](https://github.com/sbarbett/proxmox-ansible/blob/main/examples/manage-lxcs.yml) - From provisioning to final setup.
* [Example LXC dictionary](https://github.com/sbarbett/proxmox-ansible/blob/main/examples/lxcs.yml) - Defines your containers.

### Docker Compose Templates

This collection includes ready-to-use Docker Compose manifests for some common services:

* [IT Tools](https://github.com/sbarbett/proxmox-ansible/blob/main/roles/docker_compose/files/compose_files/it-tools.yml) _([Environment file](https://github.com/sbarbett/proxmox-ansible/blob/main/roles/docker_compose/files/compose_files/it-tools.env.j2))_- A collection of useful utilities for IT professionals.
* [Gitea](https://github.com/sbarbett/proxmox-ansible/blob/main/roles/docker_compose/files/compose_files/gitea.yml) _([Environment file](https://github.com/sbarbett/proxmox-ansible/blob/main/roles/docker_compose/files/compose_files/gitea.env.j2))_ -  A lightweight, self-hosted Git service.
* [PiHole-Unbound](https://github.com/sbarbett/proxmox-ansible/blob/main/roles/docker_compose/files/compose_files/pihole-unbound.yml) _([Environment file](https://github.com/sbarbett/proxmox-ansible/blob/main/roles/docker_compose/files/compose_files/pihole-unbound.env.j2))_ - A PiHole 6 container preconfigured with Unbound for upstream recursion.

## License

MIT