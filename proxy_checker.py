proxy_checker.py

import requests import concurrent.futures from core.utils import Color, slow_print

PROXY_LIST = "proxies/proxies.txt" TIMEOUT = 5

def check_proxy(proxy): try: proxies = { "http": f"http://{proxy}", "https": f"http://{proxy}" } response = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=TIMEOUT) if response.status_code == 200: return proxy except: return None

def main(): slow_print(f"{Color.CYAN}[*] Checking proxies...{Color.RESET}") try: with open(PROXY_LIST, 'r') as file: proxies = [line.strip() for line in file if line.strip()]

valid_proxies = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
        results = executor.map(check_proxy, proxies)
        for proxy in results:
            if proxy:
                valid_proxies.append(proxy)
                print(f"{Color.GREEN}[+] WORKING: {proxy}{Color.RESET}")
            else:
                print(f"{Color.RED}[-] DEAD PROXY{Color.RESET}")

    with open("proxies/working_proxies.txt", "w") as wp:
        for proxy in valid_proxies:
            wp.write(proxy + "\n")

    slow_print(f"{Color.YELLOW}[!] Total Working Proxies: {len(valid_proxies)}{Color.RESET}")

except FileNotFoundError:
    slow_print(f"{Color.RED}[!] proxies.txt file not found!{Color.RESET}")

if name == "main": main()

