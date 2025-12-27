# screenspy.py
# An importable module that captures the entire screen and saves it to a file.

from PIL import ImageGrab
import time

def capture_screen():
    """Captures the screen and saves it to a file."""
    try:
        # Take a screenshot of the screen
        screenshot = ImageGrab.grab()

        # Generate a unique filename based on the current timestamp
        file_name = f"screenshot_{int(time.time())}.png"

        # Save the screenshot to the file
        screenshot.save(file_name)

        # Print confirmation message
        print(f"[+] Screenshot saved as: {file_name}")
    
    except Exception as e:
        # Handle potential errors (e.g., no display available)
        print(f"[!] An error occurred: {e}")

# This block allows standalone execution for testing.
if __name__ == '__main__':
    capture_screen()
