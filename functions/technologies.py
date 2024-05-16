import builtwith
from colorama import Fore, Style

def check_technologies(url):
    try:
        technologies = builtwith.parse(url)
        print(f"\nTechnologies used on {url}:\n")
        for category, techs in technologies.items():
            print(f"{Fore.LIGHTBLUE_EX}{category}{Style.RESET_ALL}: {', '.join(techs)}")
    except Exception as e:
        print(f"{Fore.RED}[ERROR] {Style.RESET_ALL}Failed to retrieve technology data for {url}. Error: {e}")