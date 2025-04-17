import os
import subprocess
import sys

def install_missing_packages():
    packages = ['requests', 'colorama', 'pystyle', 'psutil']
    for pkg in packages:
        try:
            __import__(pkg)
        except ImportError:
            print(f"Installing missing package: {pkg}")
            subprocess.call([sys.executable, "-m", "pip", "install", pkg])

def check_directories():
    required_dirs = ['logs', 'attacks', 'proxies']
    for d in required_dirs:
        if not os.path.exists(d):
            os.makedirs(d)
    # Create empty logs and proxies file if missing
    if not os.path.exists("logs/attack_logs.txt"):
        open("logs/attack_logs.txt", "w").close()
    if not os.path.exists("proxies/proxies.txt"):
        open("proxies/proxies.txt", "w").close()
