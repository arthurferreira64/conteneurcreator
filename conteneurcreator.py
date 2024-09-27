import os
import subprocess
from colorama import Fore, Style

def detect_os():
    os_name = os.name
    if os_name == 'posix':
        print(Fore.GREEN + "System: Linux/Unix" + Style.RESET_ALL)
    elif os_name == 'nt':
        print(Fore.GREEN + "System: Windows" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Unknown operating system" + Style.RESET_ALL)
    return os_name

def is_docker_installed():
    try:
        subprocess.run(['docker', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(Fore.GREEN + "Docker is installed." + Style.RESET_ALL)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print(Fore.RED + "Docker is not installed." + Style.RESET_ALL)
        return False

def create_container(image_name):
    if not is_docker_installed():
        return False
    try:
        subprocess.run(['docker', 'run', '-d', image_name], check=True)
        print(Fore.GREEN + f"Container created with image {image_name}." + Style.RESET_ALL)
        return True
    except subprocess.CalledProcessError:
        print(Fore.RED + "Failed to create the container." + Style.RESET_ALL)
        return False
