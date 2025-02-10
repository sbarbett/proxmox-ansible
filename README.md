# proxmox-ansible

An Ansible role (with example playbooks) for managing Proxmox LXCs and VMs. This repository demonstrates how to provision, manage and configure Proxmox LXCs using Ansible.

## Overview

- **Role:**  
  `roles/proxmox_lxc` contains tasks for LXCs on a Proxmox server.
  
- **Examples:**  
  The `playbooks/` directory includes sample playbooks.

- **Variables:**  
  Configure API credentials (via Ansible Vault) and container definitions in the `vars/` folder.

- **Dependencies:**  
  A `bootstrap.yml` playbook is provided to install required Python libraries (`proxmoxer` and `requests`).

## Requirements

- Ansible  
- Python 3  
- A Proxmox server with API access (with an API token configured via Vault)

## Quick Start

1. **Set up your environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install ansible
   ansible-playbook -i inventory bootstrap.yml
   ```

2. Configure your vault and container definitions in `vars/`.
3. Run the playbook:

   ```bash
   ansible-playbook --vault-password-file vars/.proxmox-vault-pass playbooks/manage-lxcs.yml
   ```

## License

This project is distributed under the [MIT license](./LICENSE).