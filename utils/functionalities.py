from . import *
from utils.file_manager import load_json
from utils.input_check import check_yesno
from utils.database_manager import select, select_by_status, insert_plan

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
    pass

def dismiss_objective(db):
    pass

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
    pass

def quit_planner(db):
    db[1].close()
    db[0].close()    
    exit("See you soon!\n")

MENU_OPTIONS={"a" : ["Add a new objective", add_objective],
              "c" : ["Complete an objective", complete_objective],
              "d" : ["Dismiss an objective", dismiss_objective],
              "l" : ["List the active objectives", list_active_objectives],
              "la": ["List all the objectives", list_all_objectives],
              "ls" : ["List successful objectives", list_successful_objectives],
              "q" : ["Quit\n", quit_planner]}

def run_command(command,db):
    MENU_OPTIONS[command][1](db)