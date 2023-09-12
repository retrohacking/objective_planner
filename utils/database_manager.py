from . import *
from utils.file_manager import create_database, configure_database

def setup_database(dbname):
    db=create_database(dbname)
    configure_database(db)

def load_database(database):
    db=sqlite3.connect(database)
    cur=db.cursor()
    return db, cur


