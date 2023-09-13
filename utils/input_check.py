from . import *


def int_input(input_string=""):
    while True:
        try:
            value=int(input(input_string))
            break
        except:
            print("Please insert a valid number.")
    return value

def is_valid_option(set_of_options, option):
    if option in set_of_options.keys():
        return True, option
    else:
        return False, option
    
def check_yesno(answer):
    if answer=="y":
        return True
    else:
        return False
    
def check_valid_objective(objectives, obj):
    try:
        obj=int(obj)
    except:
        return False, obj
    for objective in objectives:
        if obj==objective[0]:
            return True, obj
    return False, obj

