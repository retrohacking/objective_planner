from . import *
from utils.file_manager import create_database, configure_database

def setup_database(dbname):
    db=create_database(dbname)
    configure_database(db)

def load_database(database):
    db=sqlite3.connect(database)
    cur=db.cursor()
    return db, cur

def select(cur, table, field):
    cur.execute(f"SELECT {field} FROM {table}")
    return cur.fetchall()

def select_by_status(cur, table, field, status):
    cur.execute(f"SELECT {field} FROM {table} WHERE status='{status}'")
    return cur.fetchall()

def insert_plan(db, plan, description):
    id=len(select(db[1], "plans", "id"))
    db[1].execute(f"INSERT INTO plans VALUES (?, ?, ?, ?, ?, 'active')", (id, plan, description, time.time(), None))
    db[0].commit()

def set_objective_as_completed(db, completed):
    db[1].execute("UPDATE plans SET end_date=?, status='completed' WHERE id=?", (time.time(), completed))
    db[0].commit()

def set_objective_as_dismissed(db, dismissed):
    db[1].execute("UPDATE plans SET end_date=?, status='dismissed' WHERE id=?", (time.time(), dismissed))
    db[0].commit()