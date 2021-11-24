import requests, time
from colorama import *
from lib.core import *
init()

try:
    tokens = open('input/tokens.txt', 'r').read().splitlines()
except:
    print(Fore.RED + 'Paste your tokens into input/tokens.txt OR create a text file named tokens')
    time.sleep(3)
    quit()
    
if len(tokens) == 0:
    print(Fore.RED + 'Paste your tokens into input/tokens.txt')
    time.sleep(3)
    quit()

def main():
    logo = '''                                                                                  
███████╗ ██████╗ █████╗ ██████╗ 
██╔════╝██╔════╝██╔══██╗██╔══██╗
███████╗██║     ███████║██████╔╝
╚════██║██║     ██╔══██║██╔══██╗
███████║╚██████╗██║  ██║██║  ██║
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝
                                      

    '''
    options = '''
    [1]: Server Join Bot / [2]: Server Leave Bot / [3]: Status Text Changer
    [4]: Status Type Changer / [5]: Message Spammer / [6]: Mass Channel Creator
    [7]: Mass Channel Deleter / [8]: Embed Message / [9]: Rainbow Role-ify
    [10]: Token Checker / [11]: Webhook Spammer / [12]: Webhook Deleter
    '''
    print(Fore.BLUE + "Thanks for buying! if not working, this means the version is outdated.")
    time.sleep(2)
    print(logo)
    time.sleep(1)
    print(Fore.BLUE + "~" * 80)
    print(options)
    print(Fore.BLUE + "~" * 80)
    print(Fore.RESET, end="")
    option = input('scar@cmd >>> ')
    features = [main_joinServer, main_leaveServer, main_statusTextChanger, main_statusTypeChanger, main_messageSpammer, main_massChannelCreator, main_massChannelDeleter, main_embedMessage, main_rainbowRole, main_tokenChecker, main_webhookSpammer, main_webhookDeleter]
    cls()
    features[int(option) - 1](tokens)
    print(Fore.BLUE + "Finished the task! Returning to menu (4)" + Fore.RESET)
    time.sleep(4)
    cls()
    main()

main()