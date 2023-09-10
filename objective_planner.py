from utils.input_check import int_input
import os

def initialization():
    print("This process is going to guide you through the configuration of the planner.\n",
          "You will have to insert some numbers before starting using it.")
    input("> OK.\n")
    print("Which is the maximum number of simultaneous plan to manage?\n",
          "You won't be able to insert more plans until you don't complete some.\n",
          "The suggested number should be below 10.")
    max_plans=int_input("> ")
    print("Which is the maximum number of objectives you could dismiss in a month?\n",
          "The suggested number should be less than the half of maximum accepted plans.")
    max_dismiss=int_input("> ")

    print(max_plans)
    print(max_dismiss)
   

def check_config():
    if not os.path.exists("config.json"):
        initialization()