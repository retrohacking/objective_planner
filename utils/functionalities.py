from . import *

def add_objective(db):
    pass

def complete_objective(db):
    pass

def dismiss_objective(db):
    pass

def list_active_objectives(db):
    pass

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
              "s" : ["List successful objectives", list_successful_objectives],
              "q" : ["Quit\n", quit_planner]}



def run_command(command,db):
    MENU_OPTIONS[command][1](db)