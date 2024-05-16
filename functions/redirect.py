from urllib.parse import urljoin
import requests
from colorama import Fore, Style

def detect_open_redirect(url):
    test_url = urljoin(url, "/?next=https://www.google.com")
    try:
        response = requests.get(test_url)
        if response.status_code == 302 and "google.com" in response.headers.get('Location', ''):
            print(f"{Fore.RED}[VULNERABLE] {Style.RESET_ALL}Open Redirect detected: {test_url}")
        else:
            print(f"{Fore.LIGHTGREEN_EX}[SAFE] {Style.RESET_ALL}No Open Redirect detected.")
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}[ERROR] {Style.RESET_ALL} Failed to test Open Redirect for {url}. Error: {e}")
