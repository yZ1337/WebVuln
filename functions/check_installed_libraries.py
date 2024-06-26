import subprocess
import sys

# Function to install packages
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_libraries():
    # Check and install python-docx if necessary
    try:
        import builtwith
    except ImportError:
        print("builtwith is not installed. Installing now...")
        install_package('builtwith')
        install_package('pandas')
        import builtwith

    # Check and install translate if necessary
    try:
        import requests
    except ImportError:
        print("requests is not installed. Installing now...")
        install_package('requests')
        import requests

    # Check and install colorama if necessary
    try:
        from colorama import Fore, Back, Style
    except ImportError:
        print("colorama is not installed. Installing now...")
        install_package('colorama')
        from colorama import Fore, Back, Style

    try:
        from bs4 import BeautifulSoup
    except ImportError:
        print("bs4 is not installed. Installing now...")
        install_package('bs4')
        from bs4 import BeautifulSoup
