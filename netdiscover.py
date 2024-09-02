#!/usr/bin/env python3

import subprocess
import sys

def run_netdiscover(ip_range):
    try:
        # Run the netdiscover command
        result = subprocess.run(
            ['sudo', 'netdiscover', '-r', ip_range],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Print the command output
        print("Netdiscover Output:\n")
        print(result.stdout)
        
        # Print any errors
        if result.stderr:
            print("Errors:\n")
            print(result.stderr)
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 run_netdiscover.py <IP_RANGE>")
        sys.exit(1)

    ip_range = sys.argv[1]
    run_netdiscover(ip_range)
