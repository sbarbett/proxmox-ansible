# container_inventory

A role to retrieve the IP address of a Proxmox LXC container using a custom Python script and dynamically add the container to Ansible’s in-memory inventory.

_Note:_ This role is intended to be used on the control node (localhost) as part of a larger workflow, ensuring that subsequent configuration roles can target the container via dynamically created inventory groups.