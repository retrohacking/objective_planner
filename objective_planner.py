from utils.config_manager import update_last_access
from utils.file_manager import create_json
from utils.input_check import int_input
from utils.window_manager import print_window, get_choice
import os

def configure():
      configs={}
      print("This process is going to guide you through the configuration of the planner.\n",
            "You will have to insert some numbers before starting using it.")
      input("> Press enter to continue.\n")
      print("Which is the maximum number of simultaneous plan to manage?\n",
            "You won't be able to insert more plans until you don't complete some.\n",
            "The suggested number should be below 10.")
      configs["max_plans"]=int_input("> ")
      print("Which is the maximum number of objectives you could dismiss in a month?\n",
            "The suggested number should be less than the half of maximum accepted plans.")
      configs["max_dismiss"]=int_input("> ")
      if (configs["max_plans"]<=configs["max_dismiss"]):
            print("You can't dismiss more plans than you have.\n")
            configure()
      else:
            create_json("config", configs)   

def initialize():
      if not os.path.exists("config.json"):
            configure()
      update_last_access()

def run():
      print_window()
      option=get_choice()