# container_extras

A role to apply additional configuration tasks on Proxmox LXC containers after the initial setup. It installs extra packages, customizes system messages, and performs other tweaks to enhance the container environment.

_Note:_ This role is intended to run on containers that have been dynamically added to the `proxmox_containers_extras` inventory group as part of a larger workflow.