
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
            [help] --> Shows the help menu
        """
        print(HelpScreen)

    def MainMenu():
        MainMenuHelp = """
                        <<Main Menu Help>>
            Basic Commands:
            [clear] --> Clears the stdout screen
            [exit]  --> Exits the session
            [menu]  --> Shows the menu
            [help]  --> Shows the help menu

            Menu Commands:
            [linode-config]             --> Enters the configuration menu for configuration of your account
            [linode-account-management] --> Enters the management menu for your Linode account
            [linode-deploymet]          --> Enters the menu for linode deployment
            [linode-networking]         --> Enters the menu for linode network configuration
        """
        print(MainMenuHelp)

# Used for Command help
class LinodeCMDHelp:
    
    def LinodeConifgHelp():
        None
    
    def LinodeAccountManagementHelp():
        None

    def LinodeDeploymentHelp():
        None
    
    def LinodeNetworkingHelp():
        None

# Used for Making configuration settings
class LinodeConfig:

    def ConnectAccount():
        None
    
# Class used for Linode cloud account manipulation
class LinodeAccountManagement:

    def ViewAccount():
        try:
            os.system('linode-cli account view')
        except:
            None

# Class used for Linode deployments
class LinodeDeployment:
    
    def MassDeploy():
        None

# Used for configuration and management of networking resources within Linode
class LinodeNetworking:

    def VPCConfig():
        None

def main():
    # Largely used variables are stored at top
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
                    
                    print("Are you sure you want to exit? Y/N")
                    ExitInput = input(": ")
                    match ExitInput:
                        case "Y":
                            os.system('cls')
                            exit()
                        case "y":
                            os.system('cls')
                            exit()
                        case "N":
                            continue
                        case "n":
                            continue
                except:
                    None      
            case "help":
                try:
                    HelpMenu.help()
                except ValueError:
                    None
            case "help menu":
                try:
                    HelpMenu.MainMenu()
                except:
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
            case "config":      
                try:
                    LinodeConfig()
                except:
                    None
                break
            case "account":
                try:
                    LinodeAccountManagement()
                except:
                    None
            case "deployment":
                try:
                    LinodeDeployment()
                except:
                    None
            case "networking":
                try:
                    LinodeNetworking()
                except:
                    None

            
                    
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
            case "menu":
                try:
                    main()
                except:
                    None
            case "exit":
                try:
                    
                    print("Are you sure you want to exit? Y/N")
                    ExitInput = input(": ")
                    match ExitInput:
                        case "Y":
                            os.system('cls')
                            exit()
                        case "y":
                            os.system('cls')
                            exit()
                        case "N":
                            continue
                        case "n":
                            continue
                except:
                    None      
            case "account":
                try:
                    LinodeAccountManagement()
                except:
                    None
            case "deployment":
                try:
                    LinodeDeployment()
                except:
                    None
            case "networking":
                try:
                    LinodeNetworking()
                except:
                    None
    
def LinodeAccountManagement():
     # Where the input is stored
    while(True):
        LinodeAccountManagementInput = input("<Account Management>:// ")
        
        match LinodeAccountManagementInput:
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
            case "menu":
                try:
                    main()
                except:
                    None
            case "exit":
                try:
                    
                    print("Are you sure you want to exit? Y/N")
                    ExitInput = input(": ")
                    match ExitInput:
                        case "Y":
                            os.system('cls')
                            exit()
                        case "y":
                            os.system('cls')
                            exit()
                        case "N":
                            continue
                        case "n":
                            continue
                except:
                    None     
            case "config":      
                try:
                    LinodeConfig()
                except:
                    None
                break
            case "deployment":
                try:
                    LinodeDeployment()
                except:
                    None
            case "networking":
                try:
                    LinodeNetworking()
                except:
                    None
def LinodeDeployment():
     # Where the input is stored
    while(True):
        LinodeDeploymentInput = input("<Deployment>:// ")
        
        match LinodeDeploymentInput:
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
            case "menu":
                try:
                    main()
                except:
                    None
            case "exit":
                try:
                    
                    print("Are you sure you want to exit? Y/N")
                    ExitInput = input(": ")
                    match ExitInput:
                        case "Y":
                            os.system('cls')
                            exit()
                        case "y":
                            os.system('cls')
                            exit()
                        case "N":
                            continue
                        case "n":
                            continue
                except:
                    None     
            case "config":      
                try:
                    LinodeConfig()
                except:
                    None
                break
            case "account":
                try:
                    LinodeAccountManagement()
                except:
                    None
            case "networking":
                try:
                    LinodeNetworking()
                except:
                    None

def LinodeNetworking():
     # Where the input is stored
    while(True):
        LinodeNetworkingInput = input("<Networking>:// ")
        
        match LinodeNetworkingInput:
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
            case "menu":
                try:
                    main()
                except:
                    None
            case "exit":
                try:
                    
                    print("Are you sure you want to exit? Y/N")
                    ExitInput = input(": ")
                    match ExitInput:
                        case "Y":
                            os.system('cls')
                            exit()
                        case "y":
                            os.system('cls')
                            exit()
                        case "N":
                            continue
                        case "n":
                            continue
                except:
                    None
            case "config":      
                try:
                    LinodeConfig()
                except:
                    None
                break
            case "account":
                try:
                    LinodeAccountManagement()
                except:
                    None
            case "deployment":
                try:
                    LinodeDeployment()
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
                


    # If there is an error within the main function or exits unexpectly
    except:
        print("Exiting...")
        exit()