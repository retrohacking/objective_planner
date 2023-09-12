from . import *


def int_input(input_string=""):
    while True:
        try:
            value=int(input(input_string))
            break
        except:
            print("Please insert a valid number.")
    return value

def is_valid_option(MENU_OPTIONS, option):
    if option in MENU_OPTIONS.keys():
        return True, option
    else:
        return False, option
    
def check_yesno(answer):
    if answer=="y":
        return True
    else:
        return False

