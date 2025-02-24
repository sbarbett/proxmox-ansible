#!/usr/bin/env python3
import sys
import argparse
from proxmoxer import ProxmoxAPI

parser = argparse.ArgumentParser(
    description="Check if a Proxmox LXC container is running."
)
parser.add_argument("--host", required=True, help="Proxmox API host")
parser.add_argument("--user", required=True, help="Proxmox API user")
parser.add_argument("--token_name", required=True, help="Proxmox API token name")
parser.add_argument("--token_value", required=True, help="Proxmox API token secret")
parser.add_argument("--node", required=True, help="Proxmox node name")
parser.add_argument("--vmid", type=int, required=True, help="VMID of the container")
args = parser.parse_args()

proxmox = ProxmoxAPI(
    args.host,
    user=args.user,
    token_name=args.token_name,
    token_value=args.token_value,
    verify_ssl=False,
)

try:
    status_info = proxmox.nodes(args.node).lxc(args.vmid).status.current.get()
    current_status = status_info.get('status')
    if current_status == 'running':
        print(f"Container {args.vmid} is running.")
        sys.exit(0)
    else:
        print(f"Container {args.vmid} exists but is not running (status: {current_status}).")
        sys.exit(1)
except Exception as e:
    print(f"Error retrieving container status: {e}", file=sys.stderr)
    sys.exit(1)
