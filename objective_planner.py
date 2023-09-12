from utils.config_manager import config_dismiss_file, configure, update_last_access
from utils.database_manager import setup_database, load_database
from utils.functionalities import run_command
from utils.window_manager import print_window, get_choice 
from utils import DATABASE, CONFIG, DISMISS
import os

def initialize():
      if not os.path.exists(CONFIG):
            configure()
      
      if not os.path.exists(DATABASE):
            setup_database(DATABASE)

      update_last_access()

      if not os.path.exists(DISMISS):
            config_dismiss_file()

def run():
      print_window()
      db=load_database(DATABASE)
      while True:
            option=get_choice()
            run_command(option, db)