import subprocess
import os
import sys
import time

# ANSI color codes for temporary use before colorama installation
ANSI_COLORS = {
    "green": "\033[92m",
    "yellow": "\033[93m",
    "red": "\033[91m",
    "cyan": "\033[96m",
    "reset": "\033[0m"
}

# Function to print colored text using ANSI escape sequences
def print_ansi(color, text):
    print(f"{ANSI_COLORS.get(color, '')}{text}{ANSI_COLORS['reset']}")

# Function to install required dependencies for this script
def install_dependency(package):
    try:
        print_ansi("yellow", f"Installing dependency '{package}'...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print_ansi("green", f"Dependency '{package}' installed successfully.")
    except subprocess.CalledProcessError as e:
        print_ansi("red", f"Failed to install '{package}'. Error: {e}")
        sys.exit(1)

# Attempt to import colorama and tqdm
try:
    import colorama
    from colorama import Fore, Style, init
except ImportError:
    install_dependency("colorama")
    import colorama
    from colorama import Fore, Style, init

try:
    from tqdm import tqdm
except ImportError:
    install_dependency("tqdm")
    from tqdm import tqdm

# Initialize colorama
init(autoreset=True)

def install_packages_from_file(file_name):
    start_time = time.time()  # Record the start time

    print("=" * 60)
    print(Fore.CYAN + "               Python Package Installer - Set 3")
    print("=" * 60)
    print(Fore.YELLOW + f"\nInstalling packages from {file_name}...\n")

    try:
        if not os.path.exists(file_name):
            print(Fore.RED + f"Error: File '{file_name}' not found.")
            return
        
        # Read the packages from the file
        with open(file_name, 'r') as file:
            packages = file.readlines()

        # Progress bar setup
        with tqdm(total=len(packages), desc="Progress", unit="pkg") as pbar:
            for package in packages:
                package = package.strip()
                if package:  # Skip any empty lines
                    print(Fore.YELLOW + f"Installing package: {package}...")

                    result = subprocess.run(
                        ["pip", "install", package],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE
                    )

                    if result.returncode == 0:
                        print(Fore.GREEN + f"Package '{package}' installed successfully.\n")
                    else:
                        print(Fore.RED + f"Failed to install package '{package}'. Error: {result.stderr.decode()}\n")
                    
                    # Update progress bar
                    pbar.update(1)
                    time.sleep(0.1)  # Optional: Simulate delay for visibility
        
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time
        minutes, seconds = divmod(execution_time, 60)

        print("=" * 60)
        print(Fore.CYAN + "          Installation process completed.")
        print(Fore.CYAN + f"          Total Execution Time: {int(minutes)} minutes {int(seconds)} seconds.")
        print("=" * 60)

    except Exception as e:
        print(Fore.RED + f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    print_ansi("cyan", "Starting Python Package Installer...")
    install_packages_from_file("set3.txt")
    input(Fore.MAGENTA + "\nPress Enter to exit...")
