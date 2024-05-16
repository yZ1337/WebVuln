import ssl
import socket
from colorama import Fore, Style

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