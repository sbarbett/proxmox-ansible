# proxmox_provision

A role to provision Proxmox LXC containers using the Proxmox API. This role creates, starts, and ensures that containers are ready for further configuration by performing necessary wait tasks and status checks.

_Note:_ This role is designed to be part of a larger workflow where container provisioning is handled first on the control node (localhost), before dynamic inventory is populated and subsequent configuration roles are executed on the target containers.