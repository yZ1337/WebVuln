import socket
from colorama import Fore, Style

def enumerate_subdomains(domain):
    try:
        subdomains = ["www", "mail", "blog", "test", "dev"]
        print(f"\nSubdomain enumeration for {domain}:\n")
        for sub in subdomains:
            subdomain = f"{sub}.{domain}"
            try:
                socket.gethostbyname(subdomain)
                print(f"{Fore.LIGHTGREEN_EX}[FOUND] {Style.RESET_ALL}{subdomain}")
            except socket.gaierror:
                print(f"{Fore.YELLOW}[NOT FOUND] {Style.RESET_ALL}{subdomain}")
    except Exception as e:
        print(f"{Fore.RED}[ERROR] {Style.RESET_ALL}Failed to enumerate subdomains for {domain}. Error: {e}")