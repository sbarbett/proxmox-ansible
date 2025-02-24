# container_setup

A role to perform the initial configuration of Proxmox LXC containers after provisioning. It executes essential tasks such as updating packages, creating a non-root user, disabling root login, and configuring SSH.

_Note:_ This role is intended to run on containers dynamically added to the `proxmox_containers` inventory group as part of a larger workflow.