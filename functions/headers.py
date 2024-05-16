import requests
from colorama import Fore, Style

def check_security_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers

        # List of recommended security headers
        recommended_headers = {
            'Content-Security-Policy': 'Helps prevent cross-site scripting attacks.',
            'X-Frame-Options': 'Protects against clickjacking.',
            'X-Content-Type-Options': 'Prevents MIME-sniffing.',
            'Strict-Transport-Security': 'Enforces secure (HTTPS) connections to the server.',
            'X-XSS-Protection': 'Enables the Cross-site scripting (XSS) filter built into most browsers, though considered deprecated as modern browsers handle XSS more effectively.',
            'Referrer-Policy': 'Governs which referrer information sent in the Referer header should be included with requests.',
            'Feature-Policy': 'Allows you to selectively enable and disable use of various browser features and APIs.',
            'Permissions-Policy': 'Controls which features and APIs can be used in the browser, a more granular and secure evolution of the Feature-Policy.',
            'Cross-Origin-Embedder-Policy (COEP)': 'Prevents a document from loading any cross-origin resources that do not explicitly grant the document permission (using CORP or CORS).',
            'Cross-Origin-Opener-Policy (COOP)': 'Isolates your origin’s browsing context from other potentially harmful origins.',
            'Cross-Origin-Resource-Policy (CORP)': 'Allows you to control the set of origins that are empowered to include your resources.',
            'Expect-CT': 'Allows sites to opt in to reporting and/or enforcement of Certificate Transparency requirements, which will prevent the use of misissued certificates for that site without being detected.'
        }

        print(f"Security headers check for: {url}\n")
        for header, description in recommended_headers.items():
            if header in headers:
                print(f"{Fore.LIGHTGREEN_EX}[PRESENT] {Style.RESET_ALL}{header}")
            else:
                print(f"{Fore.YELLOW}[MISSING] {Style.RESET_ALL}{header} - {description}")

    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}[ERROR] {Style.RESET_ALL} Failed to retrieve URL: {url}. Error: {e}")