from functions.check_installed_libraries import *
check_libraries()
from colorama import Fore, Style
import argparse
from urllib.parse import urlparse

from functions.headers import check_security_headers
from functions.technologies import check_technologies
from functions.sql_injection import test_sql_injection
from functions.ssl import check_ssl
from functions.cms import check_cms
from functions.redirect import detect_open_redirect
from functions.enum_subdomains import enumerate_subdomains
from functions.bruteforce_dirs import brute_force_directories
from functions.xss import test_xss

print(f"Created By: {Fore.LIGHTMAGENTA_EX}yZ {Style.RESET_ALL}\n")

def main():
    parser = argparse.ArgumentParser(description='Check security headers, web technologies, WAF, open redirects, CMS, subdomains, directories, SQL Injection, and XSS vulnerabilities for a given URL.')
    parser.add_argument('-u', '--url', type=str, required=True, help='URL to check')
    args = parser.parse_args()

    check_security_headers(args.url)
    check_technologies(args.url)
    check_ssl(args.url)
    check_cms(args.url)
    detect_open_redirect(args.url)
    parsed_url = urlparse(args.url)
    domain = parsed_url.netloc
    enumerate_subdomains(domain)
    brute_force_directories(args.url)
    test_sql_injection(args.url)
    test_xss(args.url)

if __name__ == '__main__':
    main()
