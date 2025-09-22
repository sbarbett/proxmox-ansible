#!/usr/bin/env python3
import sys
import time
import argparse
from proxmoxer import ProxmoxAPI

parser = argparse.ArgumentParser(
    description="Wait for a Proxmox LXC container to be registered and have the expected hostname."
)
parser.add_argument("--host", required=True, help="Proxmox API host")
parser.add_argument("--user", required=True, help="Proxmox API user")
parser.add_argument("--token_name", help="Proxmox API token name")
parser.add_argument("--token_value", help="Proxmox API token secret")
parser.add_argument("--password", help="Proxmox API password")
parser.add_argument("--node", required=True, help="Proxmox node name")
parser.add_argument("--vmid", type=int, required=True, help="VMID of the container")
parser.add_argument("--expected-hostname", required=True, help="Expected hostname for the container")
parser.add_argument("--retries", type=int, default=10, help="Number of retries")
parser.add_argument("--delay", type=int, default=3, help="Delay between retries in seconds")
args = parser.parse_args()

# Use password authentication if password is provided, otherwise use token
if args.password:
    proxmox = ProxmoxAPI(
        args.host,
        user=args.user,
        password=args.password,
        verify_ssl=False,
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
        verify_ssl=False,
    )

for attempt in range(args.retries):
    try:
        # Get the container configuration
        config = proxmox.nodes(args.node).lxc(args.vmid).config.get()
        current_hostname = config.get('hostname')
        if current_hostname == args.expected_hostname:
            print(f"Container {args.vmid} exists with expected hostname: {current_hostname}")
            time.sleep(15)
            sys.exit(0)
        else:
            sys.stderr.write(
                f"Attempt {attempt+1}: Container exists but hostname '{current_hostname}' does not match expected '{args.expected_hostname}'. Retrying in {args.delay} seconds...\n"
            )
    except Exception as e:
        sys.stderr.write(f"Attempt {attempt+1}: Container not found. Retrying in {args.delay} seconds...\n")
    time.sleep(args.delay)

sys.exit(1)
