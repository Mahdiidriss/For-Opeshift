#!/usr/bin/env python

import os
import mysql.connector
from flask import Flask


DB_HOST = os.environ['MYSQL_HOST']
DB_USER = os.environ['MYSQL_USER']
DB_PASSWORD = os.environ['MYSQL_PASSWORD']
DB_NAME = os.environ['MYSQL_DBNAME']

mydb = mysql.connector.connect(
  host=DB_HOST,
  user=DB_USER,
  password=DB_PASSWORD
)

cur = mydb.cursor()

# Execute a query
cur.execute("SELECT CURDATE()")

# Fetch one result
row = cur.fetchone()
print("Current date is: {0}".format(row[0]))

app = Flask(__name__)

@app.route("/")
def hello():
    return row

if __name__ == "__main__":
    app.run()