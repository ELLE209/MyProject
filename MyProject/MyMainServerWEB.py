# region ------------------ ABOUT -----------------------
"""
My Project...
"""
# endregion

# region ------------------ IMPORTS -----------------------

from DataBaseManager import  *

from flask import Flask, request, g, redirect, url_for, \
    abort, render_template, flash
from contextlib import closing
# endregion

# region ------------------ CONFIGURATIONS -----------------------
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
# endregion

# region ------------------ GLOBAL -----------------------
app = Flask(__name__)
data_base_manager = DataBaseManager()
# endregion


@app.route('/login')
def login():
    return 'Hello, welcome!'


@app.route('/login/<username> <password>')
def private_login(username, password):
    return 'Hello ' + username + ' ' + password + '!'
    #redirect to Service Provider
    #return redirect(('127.0.0.1', 80))

def create_db():
    fields = ["ID integer primary key autoincrement", "username text not null", "password text not null",
              "spID int not null", "spUserID int not null" ]
    data_base_manager.create_table("Users", fields)

    fields = ["SPID integer primary key autoincrement", "details text not null", "key text not null" ]
    data_base_manager.create_table("SPs", fields)


def main():
    create_db()
    app.run(host='127.0.0.1',port=8080)

if __name__ == '__main__':
    main()