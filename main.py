from check_installed_libraries import *
check_libraries()
from colorama import Fore, Style
import requests
import argparse
import builtwith
import subprocess
import os
import sys
import nmap
import ssl
import socket

print(f"Created By: {Fore.LIGHTMAGENTA_EX}yZ {Style.RESET_ALL}\n")

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

def check_technologies(url):
    try:
        technologies = builtwith.parse(url)
        print(f"\nTechnologies used on {url}:\n")
        for category, techs in technologies.items():
            print(f"{Fore.LIGHTBLUE_EX}{category}{Style.RESET_ALL}: {', '.join(techs)}")
    except Exception as e:
        print(f"{Fore.RED}[ERROR] {Style.RESET_ALL}Failed to retrieve technology data for {url}. Error: {e}")

def check_waf(url):
    try:
        wafw00f_path = os.path.join(os.path.dirname(__file__), 'wafw00f', 'wafw00f', 'main.py')
        result = subprocess.run([sys.executable, wafw00f_path, url], capture_output=True, text=True)
        output = result.stdout
        if "No WAF detected" in output:
            print(f"\nNo WAF detected on {url}.")
        else:
            print(f"\nWAF detected on {url}:\n{Fore.LIGHTGREEN_EX}{output}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[ERROR] {Style.RESET_ALL}Failed to check WAF for {url}. Error: {e}")

def scan_ports(url):
    try:
        nm = nmap.PortScanner()
        nm.scan(url)
        print(f"\nPort scan results for {url}:\n")
        for host in nm.all_hosts():
            print(f"{Fore.LIGHTBLUE_EX}Host: {host} ({nm[host].hostname()}){Style.RESET_ALL}")
            for proto in nm[host].all_protocols():
                print(f"Protocol: {proto}")
                lport = nm[host][proto].keys()
                for port in sorted(lport):
                    print(f"Port: {port}\tState: {nm[host][proto][port]['state']}")
    except Exception as e:
        print(f"\n{Fore.RED}[ERROR] {Style.RESET_ALL}Failed to scan ports for {url}. Error: {e}")

def check_ssl(url):
    try:
        hostname = url.split("//")[-1].split("/")[0]
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                print(f"\nSSL/TLS certificate for {url}:\n")
                issuer = dict(x[0] for x in cert['issuer'])
                subject = dict(x[0] for x in cert['subject'])
                print(f"{Fore.LIGHTBLUE_EX}Common Name: {Style.RESET_ALL}{subject.get('commonName')}")
                print(f"{Fore.LIGHTBLUE_EX}Issuer Country: {Style.RESET_ALL}{issuer.get('countryName')}")
                print(f"{Fore.LIGHTBLUE_EX}Issuer Organization: {Style.RESET_ALL}{issuer.get('organizationName')}")
                print(f"{Fore.LIGHTBLUE_EX}Issuer Common Name: {Style.RESET_ALL}{issuer.get('commonName')}")
                print(f"{Fore.LIGHTBLUE_EX}Valid From: {Style.RESET_ALL}{cert.get('notBefore')}")
                print(f"{Fore.LIGHTBLUE_EX}Valid Until: {Style.RESET_ALL}{cert.get('notAfter')}")
                print(f"{Fore.LIGHTBLUE_EX}Subject Alternative Names: {Style.RESET_ALL}{', '.join(x[1] for x in cert['subjectAltName'])}")
                print(f"{Fore.LIGHTBLUE_EX}OCSP: {Style.RESET_ALL}{', '.join(cert.get('OCSP', []))}")
                print(f"{Fore.LIGHTBLUE_EX}CA Issuers: {Style.RESET_ALL}{', '.join(cert.get('caIssuers', []))}")
    except Exception as e:
        print(f"{Fore.RED}[ERROR] {Style.RESET_ALL}Failed to retrieve SSL/TLS certificate for {url}. Error: {e}")

def main():
    parser = argparse.ArgumentParser(description='Check security headers, web technologies, WAF, open ports, and SSL/TLS configuration for a given URL.')
    parser.add_argument('-u', '--url', type=str, required=True, help='URL to check for security headers, web technologies, WAF, open ports, and SSL/TLS configuration')
    args = parser.parse_args()

    check_security_headers(args.url)
    check_technologies(args.url)
    check_waf(args.url)
    scan_ports(args.url)
    check_ssl(args.url)

if __name__ == '__main__':
    main()
