#!/bin/bash

# Installer script for nmap, Whois tool, and their dependencies

# Define variables
TOOL_DIR="/usr/local/src/nmap_tool"
REPO_URL="https://github.com/nmap/nmap.git"
WHOIS_SCRIPT_URL="https://github.com/iammainul/whois-ip.git"

# Function to print an error message and exit
error_exit() {
    echo "[!] $1"
    exit 1
}

# Update package lists
echo "[*] Updating package lists..."
sudo apt-get update || error_exit "Failed to update package lists."

# Install necessary dependencies for building nmap and running Python
echo "[*] Installing dependencies..."
sudo apt-get install -y git build-essential libssl-dev python3 python3-pip || error_exit "Failed to install dependencies."

# Clone the nmap repository
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

# Install python-whois
echo "[*] Installing Python Whois library..."
sudo pip3 install python-whois || error_exit "Failed to install python-whois."

# Download Whois tool script
echo "[*] Downloading Whois tool script..."
sudo curl -o /usr/local/bin/whois_tool.py $WHOIS_SCRIPT_URL || error_exit "Failed to download Whois tool script."

# Make the Whois tool script executable
sudo chmod +x /usr/local/bin/whois_tool.py || error_exit "Failed to make Whois tool script executable."

echo "[*] Whois tool installed successfully."

# Print usage instructions
echo "[*] To run the Python Whois tool, use the following command:"
echo "python3 /usr/local/bin/whois_tool.py -i <single-ip>"
echo "python3 /usr/local/bin/whois_tool.py -l <list-of-ip>"

echo "[*] To run the Python Nmap tool, use the following command:"
echo "python3 $TOOL_DIR/nmap_tool.py"
