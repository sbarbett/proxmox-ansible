# proxmox_management

This collection provides a unified solution for provisioning, configuring, and managing Proxmox LXC containers with Ansible. It bundles several roles to handle everything from container creation to advanced configuration and Docker container deployment on LXC hosts.

## Overview

The collection is composed of the following roles:

* **proxmox_provision** – Provisions and starts LXC containers on a Proxmox host using the Proxmox API.
* **container_inventory** – Retrieves each container's IP address using a custom Python script and dynamically registers the container in the Ansible inventory.
* **container_setup** – Performs initial container configuration, such as updating packages, creating non-root users, and disabling root login.
* **container_extras** – Applies additional configuration tasks as a non-root user, like installing extra packages and customizing system messages.
* **docker_compose** – Deploys and manages Docker containers on LXC hosts using Docker Compose.

These roles are designed to work together in a larger workflow that begins with provisioning containers and ends with deploying application containers via Docker.

## Requirements

* **Ansible:** Version 2.9 or later.
* **Python Libraries (on the control node):**
    - proxmoxer
    - requests
    - passlib
* **Ansible Collection Dependency:** community.general (>=6.0.0)
* **Proxmox API Access:** Valid credentials and network access to your Proxmox server.

_Note:_ I suggest using `geerlingguy.docker` for installing Docker and its plugins.

## Usage

Integrate the collection into your playbooks to create a unified workflow. For example:

```yaml
---
- name: Provision Proxmox LXC containers
  hosts: localhost
  connection: local
  gather_facts: no
  vars_files:
    - ../vars/proxmox-vault.yml
    - ../vars/lxcs.yml
  tasks:
    - name: Run proxmox_provision role for each container
      include_role:
        name: sbarbett.proxmox_management.proxmox_provision
      vars:
        container: "{{ item }}"
      loop: "{{ lxcs }}"

- name: Populate dynamic inventory with container hosts
  hosts: localhost
  connection: local
  gather_facts: no
  vars_files:
    - ../vars/proxmox-vault.yml
    - ../vars/lxcs.yml
  tasks:
    - name: Run container_setup inventory tasks for each container
      include_role:
        name: sbarbett.proxmox_management.container_inventory
        tasks_from: inventory.yml
      vars:
        container: "{{ item }}"
      loop: "{{ lxcs }}"

- name: Run initial container setup
  hosts: proxmox_containers
  gather_facts: no
  become: yes
  roles: 
    - role: sbarbett.proxmox_management.container_setup

- name: Run extras configuration on containers
  hosts: proxmox_containers_extras
  gather_facts: yes
  become: yes
  roles: 
    - role: sbarbett.proxmox_management.container_extras

- name: Run docker setup on provisioned containers
  hosts: proxmox_containers_docker
  gather_facts: yes
  roles:
    - role: geerlingguy.docker
      vars:
        docker_edition: 'ce'
        docker_service_state: started
        docker_service_enabled: true
        docker_packages:
          - "docker-{{ docker_edition }}"
          - "docker-{{ docker_edition }}-cli"
          - "docker-{{ docker_edition }}-rootless-extras"
        docker_packages_state: present
        docker_install_compose_plugin: true
        docker_compose_package: docker-compose-plugin
        docker_compose_package_state: present
        docker_users:
          - "{{ container.config.username }}"

- name: Run docker container setup on provisioned containers
  hosts: proxmox_containers_docker
  gather_facts: yes
  become: yes
  roles: 
    - role: sbarbett.proxmox_management.docker_compose
```

Your `lxcs.yml` file might look like this:

```yaml
lxcs:
  - vmid: 125
    hostname: testing
    ostemplate: "local:vztmpl/debian-12-standard_12.7-1_amd64.tar.zst"
    storage: "local-lvm"
    cores: 1
    memory: 1024
    swap: 512
    disk: "local-lvm:25"
    net: "name=eth0,bridge=vmbr0,ip=dhcp"
    password: "containerpassword"
    onboot: true
    pubkey_file: "~/.ssh/id_rsa.pub"
    features: "nesting=1"
    # Additional configuration
    config:
      username: demo
      user_password: "demo123"
      private_key: "~/.ssh/id_rsa"
      wait_for_status: true
      initial_setup: true
      install_extras: true
      install_docker: true
      docker_containers:
        it-tools:
          port: 8582
        gitea:
          port_http: 3000
          port_ssh: 222
```

## License

MIT