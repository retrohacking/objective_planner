from . import *

def create_json(filename, data):
    if not ".json" in filename:
        filename+=".json"
    jsondata=json.dumps(data, indent=4)
    file=open(filename, "w")
    file.write(jsondata)
    file.close()

def create_database(dbname):
    return sqlite3.connect(dbname)

def configure_database(db):
    cur=db.cursor()
    cur.execute("CREATE TABLE plans(id, plan, description, start_date, end_date, status) ")
