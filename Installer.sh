#!/bin/bash

# Installer script for whois, dig, nmap, and their dependencies

# Define variables
TOOL_DIR="/usr/local/src/information_gathering_tool"
PYTHON_SCRIPT="information_gathering_tool.py"

# Function to print an error message and exit
error_exit() {
    echo "[!] $1"
    exit 1
}

# Update package lists
echo "[*] Updating package lists..."
sudo apt-get update || error_exit "Failed to update package lists."

# Install necessary dependencies for whois, dig, nmap, and running Python
echo "[*] Installing dependencies..."
sudo apt-get install -y whois dnsutils nmap python3 python3-pip || error_exit "Failed to install dependencies."

echo "[*] All tools and dependencies installed successfully."

# Ensure the Python script is available in the TOOL_DIR
if [ ! -f "$TOOL_DIR/$PYTHON_SCRIPT" ]; then
    echo "[!] Python script $PYTHON_SCRIPT not found in $TOOL_DIR."
    echo "[*] Please place the $PYTHON_SCRIPT in $TOOL_DIR and run it using the following command:"
    echo "python3 $TOOL_DIR/$PYTHON_SCRIPT"
else
    echo "[*] Python script found. To run the Python tool, use the following command:"
    echo "python3 $TOOL_DIR/$PYTHON_SCRIPT"
fi
