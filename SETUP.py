import subprocess
import sys
import importlib
import platform

packages = ["pwinput", "cryptography", "pyperclip", "rstr"]
files = ["create_db.py", "edit_db.py", "retrieve_db.py", "generate_passwd.py"]

# this installs all required packages
for package in packages:
    try:
        importlib.import_module(package)
        print(f"{package} is already installed.")
    except ImportError:
        print(f"Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        importlib.import_module(package)

# this alerts you if you use linux
if platform.system() == "Linux":
    print("Linux detected. For clipboard support, make sure one of the following is installed:")
    print("  - xclip: sudo apt install xclip")
    print("  - OR xsel: sudo apt install xsel")
    print("  - OR wl-clipboard (for Wayland): sudo apt install wl-clipboard")
    print("And scrolling is not natively supported. Sorry.")

    for file in files:
        subprocess.run(["chmod", "+x", file])

    print("Successfully made all files executable.")