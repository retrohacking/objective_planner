from . import *

def add_objective():
    pass

def complete_objective():
    pass

def dismiss_objective():
    pass

def list_active_objectives():
    pass

def list_successful_objectives():
    pass

def quit_planner():
    exit("See you soon!\n")

MENU_OPTIONS={"a" : ["Add a new objective", add_objective],
              "c" : ["Complete an objective", complete_objective],
              "d" : ["Dismiss an objective", dismiss_objective],
              "l" : ["List the active objectives", list_active_objectives],
              "s" : ["List successful objectives", list_successful_objectives],
              "q" : ["Quit\n", quit_planner]}



def run_command(command):
    MENU_OPTIONS[command][1]()