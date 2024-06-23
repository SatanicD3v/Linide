
""""
 This is a small framework that allows you to work with your
 Linode Cloud Environment without typing every single command
 or going inside the web gui

 This program was written by: Trent Schake

 There is no warrenty within this program
 and the author of this software is not responsible
 for any damages caused by this software.

 Please use at your own risk.

"""

import threading
import os
import requests
import sys
import time

# Class used for accessing different elements of the help screen
class HelpMenu:
    
    # Main Help Screen
    def help():
        HelpScreen = """
                        <<Help>>
            Basic MainMenu Commands
            [clear] --> Clears the stdout screen
            [exit] --> Exits the session
            [menu] --> Shows the menu 
            [help] --> Shows the help display
            [linode-config] --> Enters configuration for linode settinsg
        """
        print(HelpScreen)

# Class used for Linode cloud account manipulation
class LinodeAccount:

    def GetAccount():
        os.system('linodecli')


def main():
    # Largely used variables are stored at top
    OperatingSystems = ["nt","posix"]
    ClearScreen = os.system('cls')
    global MenuPage
    MenuPage = """
    =====================================================
                       <<<Linide>>>
                 <<Framework for Linode>>                
                        <<Ver 1.0>>            
               [Please read the documentation
            prior to working with this framework]
    =====================================================
        
    """
    print(MenuPage)
    while(True):
        # This is where the main console line is located        
        MainUserInput = input("<MainMenu>:// ")
        match MainUserInput:
            case "exit":
                try:
                    MainUserInput = None
                    exit()
                except ValueError:
                     None
            case "help":
                try:
                    HelpMenu.help()
                except ValueError:
                    None
            case "clear":
                try:
                    os.system('cls')
                except:
                    None
            case "menu":
                try:
                    print(MenuPage)
                except:
                    None
            case "linode-config":      
                LinodeConfigThread = threading.Thread(target=LinodeConfig)
                try:
                    LinodeConfigThread.start()
                    LinodeConfigThread.join()
                except:
                    if LinodeConfigThread == False:
                        print("Warning!! There was a threading issue with the Linode Configuration Thread that caused an internal error!")
                        time.sleep(1)
                break
    

            
                    
# Function that is used to work with configurations within the linode
def LinodeConfig():
    # Where the input is stored
    while(True):
        LinodeConfigInput = input("<Config>:// ")
        
        match LinodeConfigInput:
            case "clear":
                try:
                    os.system('cls')
                except:
                    None
            case "help":
                try:
                    HelpMenu.help()
                except:
                    None
            case "back":
                try:
                    main()
                except:
                    None
    



    


# Makes a function call to main if there are no errors
if __name__ == '__main__':
    try:
        MainThread = threading.Thread(target=main())
        # Starts the thread within main and places it inside a try and except
        try:
            # Starts the thread that performs a function call to main
            MainThread.start()
            MainThread.join()
        except:
            # If the thread returns a false value and fails
            if MainThread == False:
                print("WARNING! There is an issue with a thread that caused an internal error.")
                



    except:
        print("Exiting...")
        exit()