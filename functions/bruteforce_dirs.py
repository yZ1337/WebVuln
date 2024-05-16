from urllib.parse import urljoin
import requests
from colorama import Fore, Style

def brute_force_directories(url):
    directories = ["admin", "login", "dashboard", "config", "backup", "robots.txt", "sitemap.xml"]
    print(f"\nDirectory brute-forcing for {url}:\n")
    for directory in directories:
        dir_url = urljoin(url, directory)
        try:
            response = requests.get(dir_url)
            if response.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[FOUND] {Style.RESET_ALL}{dir_url}")
            else:
                print(f"{Fore.YELLOW}[NOT FOUND] {Style.RESET_ALL}{dir_url}")
        except requests.exceptions.RequestException as e:
            print(f"{Fore.RED}[ERROR] {Style.RESET_ALL}Failed to brute-force directory {dir_url}. Error: {e}")
