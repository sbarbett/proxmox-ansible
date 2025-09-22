# proxmox_provision

A role to provision Proxmox LXC containers using the Proxmox API. This role creates, starts, and ensures that containers are ready for further configuration by performing necessary wait tasks and status checks.

## Authentication

This role supports both API token and password authentication:

### API Token Authentication (Recommended for most use cases)
```yaml
proxmox_api_user: "root@pam"
proxmox_api_id: "ansible"
proxmox_api_secret: "your-token-secret"
```

### Password Authentication
```yaml
proxmox_api_user: "root@pam"
proxmox_api_password: "your-root-password"
```

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `vmid` | Container VM ID | Yes |
| `hostname` | Container hostname | Yes |
| `ostemplate` | OS template to use | Yes |
| `storage` | Storage for container | Yes |
| `cores` | Number of CPU cores | Yes |
| `memory` | Memory in MB | Yes |
| `swap` | Swap memory in MB | Yes |
| `disk` | Disk configuration | Yes |
| `net` | Network configuration | Yes |
| `password` | Root password for container | No |
| `onboot` | Start container on boot | No |
| `startup` | Startup configuration | No |
| `pubkey_file` | SSH public key file path | No |
| `features` | Container features | No |
| `mounts` | Additional mount points | No |

_Note:_ This role is designed to be part of a larger workflow where container provisioning is handled first on the control node (localhost), before dynamic inventory is populated and subsequent configuration roles are executed on the target containers.