#!/bin/bash

# Installer script for nmap, whois, and their dependencies

# Define variables
TOOL_DIR="/usr/local/src/nmap_tool"
REPO_URL="https://github.com/nmap/nmap.git"
PYTHON_SCRIPT="nmap_tool.py"

# Function to print an error message and exit
error_exit() {
    echo "[!] $1"
    exit 1
}

# Update package lists
echo "[*] Updating package lists..."
sudo apt-get update || error_exit "Failed to update package lists."

# Install necessary dependencies for building nmap, whois, and running Python
echo "[*] Installing dependencies..."
sudo apt-get install -y git build-essential libssl-dev python3 python3-pip whois || error_exit "Failed to install dependencies."

# Clone the nmap repository if not already present
if [ ! -d "$TOOL_DIR/nmap" ]; then
    echo "[*] Cloning nmap repository..."
    sudo git clone --depth=1 $REPO_URL "$TOOL_DIR/nmap" || error_exit "Failed to clone nmap repository."
else
    echo "[*] Nmap repository already exists."
fi

# Compile and install nmap
echo "[*] Installing nmap..."
cd "$TOOL_DIR/nmap" || error_exit "Failed to change directory to $TOOL_DIR/nmap."
sudo ./configure && sudo make && sudo make install || error_exit "Failed to install nmap."

echo "[*] Nmap installed successfully."

# Check for the existence of the Python script
if [ ! -f "$TOOL_DIR/$PYTHON_SCRIPT" ]; then
    echo "[!] Python script $PYTHON_SCRIPT not found in $TOOL_DIR."
    echo "[*] Please place the $PYTHON_SCRIPT in $TOOL_DIR and run it using the following command:"
    echo "python3 $TOOL_DIR/$PYTHON_SCRIPT"
else
    echo "[*] Python script found. To run the Python tool, use the following command:"
    echo "python3 $TOOL_DIR/$PYTHON_SCRIPT"
fi

# Check for whois installation
if ! command -v whois &> /dev/null; then
    echo "[!] Whois tool is not installed."
    echo "[*] Installing whois..."
    sudo apt-get install -y whois || error_exit "Failed to install whois."
else
    echo "[*] Whois tool is already installed."
fi

echo "[*] All tools installed successfully. You can now use the nmap and whois tools."
