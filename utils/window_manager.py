from . import *
from utils.functionalities import MENU_OPTIONS
from utils.input_check import is_valid_option

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

def print_options():
    for key in MENU_OPTIONS.keys():
        print(f"{key} - {MENU_OPTIONS[key][0]}")

def print_window():
    print_banner()
    print_options()

def get_choice():
    valid_option=False
    while not valid_option:
        valid_option, option=is_valid_option(input("> ").lower())
        if valid_option:
            return option
        else:
            print("Please insert a valid option.")