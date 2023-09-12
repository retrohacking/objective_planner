from . import *
from utils.file_manager import create_json
from utils.input_check import int_input

def update_last_access():
    configfile=open("config.json","r")
    jsondict=json.load(configfile)
    jsondict["last_access"]=time.localtime()
    jsondata=json.dumps(jsondict, indent=4)
    configfile.close()
    configfile=open("config.json","w")
    configfile.write(jsondata)
    configfile.close()

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
        configs["residual_dismiss"]=configs["max_dismiss"]
        configs["last_dismiss_reset"]=time.localtime()
        create_json("config", configs)   

def load_config(file):
    configfile=open(file, "r")
    jsonfile=json.load(configfile)
    configfile.close()
    return jsonfile

def config_dismiss_file():
    config={}
    configjson=load_config(CONFIG)
    config["residual_dismiss"]=configjson["max_dismiss"]
    config["last_dismiss_reset"]=time.localtime()
    create_json(DISMISS, config)
