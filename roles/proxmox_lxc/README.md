Role Name
=========

**proxmox_lxc**  
An Ansible role for managing Proxmox LXC containers. This role allows you to create or manage LXCs on a Proxmox server using the Proxmox API.

Requirements
------------

- **Proxmox Server:** You must have a Proxmox server with API access.
- **API Token:** The role assumes that you are using an API token (with or without privilege separation, as needed) for authentication.
- **Python Dependencies:** The role uses the Proxmox community modules which require the Python libraries `proxmoxer` and `requests`. Make sure these are installed (e.g. via a bootstrap playbook).

Role Variables
--------------

The following variables are used by this role. Some are defined in `defaults/main.yml` and can be overridden in your playbook or inventory:

- **proxmox_api_host:**  
  *(Default: "proxmox.example.com")*  
  The hostname or IP address of your Proxmox server.

- **proxmox_node:**  
  *(Default: "pve")*  
  The name of the Proxmox node where the container will be managed.

The role also expects a set of variables for each container, passed in as a dictionary (typically via a list loop in your playbook). These include:

- **container.vmid:**  
  The unique ID of the LXC container.

- **container.hostname:**  
  The hostname for the container.

- **container.ostemplate:**  
  The OS template to use for the LXC (e.g., `"local:vztmpl/debian-12-standard_12.7-1_amd64.tar.zst"`).

- **container.storage:**  
  The storage volume name (e.g., `"local-lvm"`).

- **container.cores:**  
  The number of vCPU cores allocated to the container.

- **container.memory:**  
  The amount of RAM (in MB) allocated to the container.

- **container.swap:**  
  The swap space (in MB) for the container.

- **container.disk:**  
  The disk configuration in the format `"storage_name:size_in_GB"` (e.g., `"local-lvm:25"`).

- **container.net:**  
  Network configuration (e.g., `"name=eth0,bridge=vmbr0,ip=dhcp"`).

- **container.password:**  
  The root password for the container.

- **container.state:**  
  Desired state of the container. Use `"present"` to create/update the container and `"absent"` to delete it.

Dependencies
------------

This role has no external role dependencies. It relies solely on the Proxmox community modules and Python libraries (`proxmoxer`, `requests`), so ensure they are installed as part of your environment setup.