from . import *
from utils.input_check import is_valid_option
from utils.functionalities import MENU_OPTIONS, print_options

def print_banner():

    print("""
     ██████╗ ██████╗      ██╗███████╗ ██████╗████████╗██╗██╗   ██╗███████╗███████╗
    ██╔═══██╗██╔══██╗     ██║██╔════╝██╔════╝╚══██╔══╝██║██║   ██║██╔════╝██╔════╝
    ██║   ██║██████╔╝     ██║█████╗  ██║        ██║   ██║██║   ██║█████╗  ███████╗
    ██║   ██║██╔══██╗██   ██║██╔══╝  ██║        ██║   ██║╚██╗ ██╔╝██╔══╝  ╚════██║
    ╚██████╔╝██████╔╝╚█████╔╝███████╗╚██████╗   ██║   ██║ ╚████╔╝ ███████╗███████║
     ╚═════╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝   ╚═╝  ╚═══╝  ╚══════╝╚══════╝
                                                                                
    ██████╗ ██╗      █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗                   
    ██╔══██╗██║     ██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗                  
    ██████╔╝██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝                  
    ██╔═══╝ ██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗                  
    ██║     ███████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║                  
    ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝                  
                                                                              """)
    print(f"\t\t\t\t\t{AUTHOR} - {YEAR}\tv{VERSION}")
    print(f"\t\t\t\t\t{GITHUB}")
    print("\n\n")


def print_window():
    print_banner()
    print_options()

def get_choice():
    valid_option=False
    while not valid_option:
        print("Insert your option")
        valid_option, option=is_valid_option(MENU_OPTIONS, input("> ").lower())
        if valid_option:
            return option
        else:
            print("Please insert a valid option.\n")