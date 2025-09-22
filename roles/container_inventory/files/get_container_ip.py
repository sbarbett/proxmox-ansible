#!/usr/bin/env python3
import sys
import time
import argparse
from proxmoxer import ProxmoxAPI

parser = argparse.ArgumentParser(
    description="Retrieve container IP from Proxmox with retries"
)
parser.add_argument("--host", required=True, help="Proxmox API host")
parser.add_argument("--user", required=True, help="Proxmox API user")
parser.add_argument("--token_name", help="Proxmox API token name")
parser.add_argument("--token_value", help="Proxmox API token secret")
parser.add_argument("--password", help="Proxmox API password")
parser.add_argument("--node", required=True, help="Proxmox node name")
parser.add_argument("--vmid", type=int, required=True, help="VMID of the container")
parser.add_argument("--retries", type=int, default=10, help="Number of retries")
parser.add_argument("--delay", type=int, default=3, help="Delay between retries in seconds")
args = parser.parse_args()

# Use password authentication if password is provided, otherwise use token
if args.password:
    proxmox = ProxmoxAPI(
        args.host,
        user=args.user,
        password=args.password,
        verify_ssl=False
    )
else:
    if not args.token_name or not args.token_value:
        print("Error: Either password or token_name and token_value must be provided", file=sys.stderr)
        sys.exit(1)
    proxmox = ProxmoxAPI(
        args.host,
        user=args.user,
        token_name=args.token_name,
        token_value=args.token_value,
        verify_ssl=False
    )

ip_address = None
for attempt in range(args.retries):
    try:
        interfaces = proxmox.nodes(args.node).lxc(args.vmid).interfaces.get()
    except Exception as e:
        sys.stderr.write(f"Attempt {attempt+1}: Error retrieving interfaces: {e}\n")
        time.sleep(args.delay)
        continue

    for interface in interfaces:
        if interface.get("name") == "eth0":
            inet = interface.get("inet")
            if inet:
                ip_address = inet.split("/")[0]
                break

    if ip_address:
        print(ip_address)
        sys.exit(0)
    else:
        sys.stderr.write(f"Attempt {attempt+1}: eth0 not found or no IP assigned. Retrying in {args.delay} seconds...\n")
        time.sleep(args.delay)

sys.stderr.write("Failed to retrieve container IP address after multiple attempts.\n")
sys.exit(1)
