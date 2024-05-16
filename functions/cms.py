import requests
from colorama import Fore, Style

def check_cms(url):
    try:
        response = requests.get(url)
        if "wp-content" in response.text or "wp-includes" in response.text:
            print(f"{Fore.LIGHTGREEN_EX}WordPress CMS detected{Style.RESET_ALL}")
        elif "Joomla" in response.text:
            print(f"{Fore.LIGHTGREEN_EX}Joomla CMS detected{Style.RESET_ALL}")
        elif "Drupal" in response.text:
            print(f"{Fore.LIGHTGREEN_EX}Drupal CMS detected{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}No common CMS detected{Style.RESET_ALL}")
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}[ERROR] {Style.RESET_ALL} Failed to check CMS for {url}. Error: {e}")