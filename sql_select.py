import sqlite3
import os
import threading

lock = threading.Lock()

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


filepath = "test.db"
if os.path.exists(filepath):
    conn = sqlite3.connect(filepath, check_same_thread=False) 
    conn.row_factory = dict_factory
else:
    raise Exception("Database file not found")

with lock:
    cur = conn.cursor()
    cur.execute("SELECT * FROM station")
    items_list = cur.fetchall()
print(items_list)