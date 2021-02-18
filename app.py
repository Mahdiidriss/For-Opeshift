#!/usr/bin/env python

import sys
import _mysql
from flask import Flask
import MySQLdb as mdb

DB_HOST = os.environ[MYSQL_HOST]
DB_USER = os.environ[MYSQL_USER]
DB_PASSWORD = os.environ[MYSQL_PASSWORD]
DB_NAME = os.environ[MYSQL_DBNAME]

con = _mysql.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)        
con.query("SELECT VERSION()")
result = con.use_result()
version = result.fetch_row()[0]



app = Flask(__name__)

@app.route("/")
def hello():
    return version

if __name__ == "__main__":
    app.run()