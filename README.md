# Chimera Cybersecurity Toolkit

Chimera is a cybersecurity learning tool developed to simulate various malware payloads. It serves as an educational toolkit for ethical hacking and cybersecurity enthusiasts. This project showcases key cybersecurity concepts and techniques, such as file encryption, ransomware simulation, keystroke logging, popup spam, data theft, and persistence mechanisms.

---

## **Features**
This project includes the following payloads and simulations:
1. **Ransomware Simulation (`ransomware.py`)**:
   - Encrypts files in a specified directory using AES encryption (via `cryptography` library).
   - Generates a unique decryption key for each encryption session.
   - Creates a ransom note with instructions for decrypting the files.

2. **Decryptor (`decryptor.py`)**:
   - Provides an interface to decrypt files encrypted by the ransomware simulation.
   - Validates the decryption key and restores files to their original state.

3. **Keylogger (`keylogger.py`)**:
   - Captures and logs keystrokes in real-time using the `pynput` library.
   - Saves logs to a file for review.

4. **File Infostealer (`infostealer.py`)**:
   - Identifies and copies sensitive files (e.g., `.docx`, `.pdf`) from a directory to a target location.

5. **Popup Spam (`popup_spam.py`)**:
   - Generates disruptive popup messages to simulate intrusive payload behavior.

6. **Persistence Mechanism (`persistenc.py`)**:
   - Adds Chimera to startup programs to ensure it runs automatically after reboot.

---

## **Tech Stack**
This project is built entirely in Python and relies on several libraries for functionality:
- **`cryptography`**: Used for secure AES file encryption.
- **`pynput`**: Used for creating the keylogger.
- **`colorama`**: Provides colored terminal output to enhance UI clarity.
- **Built-in Python libraries (`shutil`, `os`, `sys`)**: Handle file manipulation, system processes, and directory traversal.

---

## **Installation**
Follow these steps to set up Chimera on your local machine:

### **Prerequisites**
- **Python Version**: Ensure Python 3.8+ is installed.
- **Dependencies**: You can install the required Python libraries using the `requirements.txt`.

### **Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/HediDhakar/chimera-project.git
   cd chimera-project
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run Chimera:
   ```bash
   python3 chimera.py
   ```

---

## **Usage**
Upon running `chimera.py`, an interactive menu will appear. Use the menu to select a payload and execute it.


### **Testing**
You can use dummy files in a separate test directory to safely demonstrate ransomware and infostealer functionalities.

---

## **Disclaimer**
> ⚠️ **Ethical Use Only**:
This tool is strictly intended for **educational purposes**. Do not use it for malicious activities or unauthorized penetration testing. Misuse of this software can lead to serious legal consequences. The developer is not responsible for any harm caused by unethical usage.

---

## **How It Works**
### **1. Ransomware Simulation (`ransomware.py`)**
- **Input**: Path to the directory containing target files.
- **Process**:
   - Encrypts each file in the directory.
   - Saves the `.txt` decryption key and ransom note.
- **Output**: Files are replaced with encrypted versions, and a ransom note appears.

### **2. Keylogger (`keylogger.py`)**
- **Input**: Captures keystrokes of the user.
- **Process**: Copies every key press to a `.log` file.
- **Output**: Log file of captured keystrokes.

### **3. Persistence Mechanism (`persistenc.py`)**
- **Input**: Adds Chimera to system startup.
- **Process**: Writes registry entries (Windows) or modifies `.bashrc` (Linux).
- **Output**: Chimera runs automatically at startup.

---

## **Code Highlights**
### **Encryption in `ransomware.py`**
```python
from cryptography.fernet import Fernet

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()
    encrypted_data = Fernet(key).encrypt(data)
    with open(file_path, 'wb') as f:
        f.write(encrypted_data)
```

### **Keystroke Logging in `keylogger.py`**
```python
from pynput.keyboard import Listener

def log_keystrokes(output_file):
    with Listener(on_press=lambda key: write_to_file(output_file, str(key))) as listener:
        listener.join()
```

### **Popup Spam in `popup_spam.py`**
```python
from tkinter import Tk, messagebox

def spam_popup():
    root = Tk()
    root.withdraw()
    messagebox.showerror("Warning!", "This is a sample popup spam!")
```

---

## **Contributing**
We welcome contributions to improve Chimera! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add <feature>"
   ```
4. Push your branch and submit a pull request!

---

## **Contact**
For questions, suggestions, or collaboration, feel free to contact me:
- GitHub: [HediDhakar](https://github.com/HediDhakar)
- Email: [hedidk63@gmail.com]

---
