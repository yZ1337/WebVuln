import requests
from colorama import Fore, Style

def test_xss(url):
    param = "q"
    payload = "<script>alert('XSS')</script>"
    print(f"\nXSS test for {url}:\n")
    test_url = f"{url}?{param}={payload}"
    try:
        response = requests.get(test_url)
        if payload in response.text:
            print(f"{Fore.RED}[VULNERABLE] {Style.RESET_ALL}Possible XSS: {test_url}")
        else:
            print(f"{Fore.LIGHTGREEN_EX}[SAFE] {Style.RESET_ALL}No XSS detected.")
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}[ERROR] {Style.RESET_ALL} Failed to test XSS for {url}. Error: {e}")