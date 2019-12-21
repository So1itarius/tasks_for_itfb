import os
import sqlite3

path = "data-3895-2019-11-30.json"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "trade fairs.sqlite")

con = sqlite3.connect(db_path)