# region ------------------ ABOUT -----------------------
"""
My Project...
"""
# endregion

# region ------------------ IMPORTS -----------------------
import sqlite3
from flask import Flask, request, g, redirect, url_for, \
    abort, render_template, flash
from contextlib import closing
# endregion

# region ------------------ CONFIGURATIONS -----------------------
#DATABASE = 'C:\Users\Elizabeth\MyDB.db'
DATABASE = 'C:\Users\Elizabeth\Documents\GitHub\MyProject\MyProject\databases\MyDB.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
# endregion


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db0():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def init_db():
    with closing(connect_db()) as db:
        cursor = db.cursor().execute("select ID, username, password from users where username = 'elle' and spID = 1")

        for row in cursor.fetchall():
            id, username, password = row
            print ' {%d}: %s, %s' % (id, username, password)

def init_db2():
    db = closing(connect_db())
    f = app.open_resource('schema.sql', mode='r')

    db.cursor().executescript(f.read())
    db.commit()

if __name__ == '__main__':
    app = Flask(__name__)
    app.config.from_object(__name__)
    init_db()
    app.run()
