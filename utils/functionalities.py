from . import *
from utils.file_manager import load_json, create_json
from utils.input_check import check_yesno, check_valid_objective
from utils.database_manager import select, select_by_status, insert_plan, set_objective_as_completed, set_objective_as_dismissed


def add_objective(db):
    configjson=load_json(CONFIG)
    max_objectives=configjson["max_plans"]
    active_objectives=len(select_by_status(db[1], 'plans', 'plan', 'active'))
    if (active_objectives>=max_objectives):
        print("You cannot insert another objective. You have reached the maximum number")
    else:
        print("Insert the name of the plan")
        plan=input("> ")
        print("Insert the description for this plan")
        description=input(">")
        print("Do you want to insert this plan? (Y/N)")
        print(f"{plan} - {description}")
        if check_yesno(input("> ").lower()):
            insert_plan(db, plan, description)
            print("Plan inserted correctly!\n")
        else:
            print("The plan has not been added.\n")
            return

def complete_objective(db):
    print("Insert the ID of the completed objective:")
    list_active_objectives(db)
    objectives=select_by_status(db[1], 'plans', '*', 'active')
    for i in range(3):
        completed=input("> ")
        valid_option, completed=check_valid_objective(objectives, completed)
        if not valid_option:
            print("Please insert a valid objective to set as completed")
            if i==2:
                print("Returning to home selection\n")
            continue
        else:
            set_objective_as_completed(db, completed)
            print("GREAT! KEEP IT UP!\n")
            break
    
def dismiss_objective(db):
    jsonfile=load_json(DISMISS)
    residual_dismissions=jsonfile["residual_dismiss"]
    if residual_dismissions==0:
        print("You have not residual dismissions for this month!\n")
        return
    else:
        print("Which objective do you want to dismiss?")
        list_active_objectives(db)
        objectives=select_by_status(db[1], 'plans', '*', 'active')
        for i in range(3):
            dismissed=input("> ")
            valid_option, dismissed=check_valid_objective(objectives, dismissed)
            if not valid_option:
                print("Please insert a valid objective to dismiss")
                if i==2:
                    print("Returning to home selection\n")
                continue
            else:
                set_objective_as_dismissed(db, dismissed)
                residual_dismissions-=1
                jsonfile["residual_dismiss"]=residual_dismissions
                create_json(DISMISS, jsonfile)
                print("Don't worry! Better luck next time\n")
                break



def list_active_objectives(db):
    active_objectives=select_by_status(db[1], 'plans', '*', 'active')
    for obj in active_objectives:
        print(f"[{obj[0]}] {obj[1]} - {obj[2]}")
    print("")

def list_all_objectives(db):
    objectives=select(db[1], 'plans', '*')
    for obj in objectives:
        print(f"[{obj[0]}] {obj[1]} - {obj[2]}\t[{obj[5]}]")
    print("")

def list_successful_objectives(db):
    active_objectives=select_by_status(db[1], 'plans', '*', 'completed')
    for obj in active_objectives:
        start_date=time.strftime('%Y/%m/%d', time.localtime(obj[3]))
        end_date=time.strftime('%Y/%m/%d', time.localtime(obj[4]))
        print(f"[{obj[0]}] {obj[1]}\t|\tStart: {start_date} - End: {end_date}")
    print("")


def print_options(db=None):
    for key in MENU_OPTIONS.keys():
        print(f"{key} - {MENU_OPTIONS[key][0]}")

def quit_planner(db):
    db[1].close()
    db[0].close()    
    exit("See you soon!\n")

MENU_OPTIONS={"a" : ["Add a new objective", add_objective],
              "c" : ["Complete an objective", complete_objective],
              "d" : ["Dismiss an objective", dismiss_objective],
              "l" : ["List all the objectives", list_all_objectives],
              "la": ["List the active objectives", list_active_objectives],
              "ls": ["List successful objectives", list_successful_objectives],
              "h" : ["Show this guide", print_options],
              "q" : ["Quit\n", quit_planner]}

def run_command(command,db):
    MENU_OPTIONS[command][1](db)