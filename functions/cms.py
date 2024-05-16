import requests
from colorama import Fore, Style

def check_cms(url):
    try:
        response = requests.get(url)
        if "wp-content" in response.text or "wp-includes" in response.text:
            print(f"\n{Fore.LIGHTGREEN_EX}WordPress CMS detected{Style.RESET_ALL}")
            print(f"\n{Fore.LIGHTBLUE_EX}[INFO] {Style.RESET_ALL}Use wpscan to find WordPress vulnerabilities.")
        elif "Joomla" in response.text:
            print(f"\n{Fore.LIGHTGREEN_EX}Joomla CMS detected{Style.RESET_ALL}")
        elif "Drupal" in response.text:
            print(f"\n{Fore.LIGHTGREEN_EX}Drupal CMS detected{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.YELLOW}No common CMS detected{Style.RESET_ALL}")
    except requests.exceptions.RequestException as e:
        print(f"\n{Fore.RED}[ERROR] {Style.RESET_ALL} Failed to check CMS for {url}. Error: {e}")
