#!/bin/bash

# Dracula Install Script for 404_Vampire-DDos-X

clear
echo -e "\033[1;91m[!] Installing 404_Vampire-DDos-X requirements...\033[0m"

# Function: Auto-fix missing dependencies
fix_packages() {
    echo -e "\n\033[1;92m[*] Fixing packages and dependencies...\033[0m"
    apt update -y && apt upgrade -y
    apt install -y python3 python3-pip curl wget git net-tools
    pkg install -y python3 python3-pip curl wget git net-tools 2>/dev/null
}

# Step 1: Ensure Python and pip are installed
if ! command -v python3 >/dev/null 2>&1; then
    echo -e "\033[1;91m[-] Python3 not found! Installing...\033[0m"
    fix_packages
fi

if ! command -v pip3 >/dev/null 2>&1; then
    echo -e "\033[1;91m[-] pip3 not found! Installing...\033[0m"
    apt install -y python3-pip || pkg install -y python3-pip
fi

# Step 2: Install Python packages
echo -e "\n\033[1;92m[*] Installing Python requirements...\033[0m"
pip3 install --upgrade pip
pip3 install -r requirements.txt || pip install -r requirements.txt

# Step 3: Check for logs & proxies folders
[ -d "logs" ] || mkdir logs
[ -f "logs/attack_logs.txt" ] || touch logs/attack_logs.txt

[ -d "proxies" ] || mkdir proxies
[ -f "proxies/proxies.txt" ] || touch proxies/proxies.txt

# Step 4: Make main script executable
chmod +x vampire_ddos_x.py
chmod +x proxy_checker.py

# Done
echo -e "\n\033[1;92m[✓] Installation completed successfully!\033[0m"
echo -e "\033[1;96m[!] Run the tool using:\033[0m python3 vampire_ddos_x.py"
