# region ------------------ ABOUT -----------------------
"""
My Project...
"""
# endregion

# region ------------------ IMPORTS -----------------------

from DataBaseManager import *

from flask import Flask, request, g, redirect, url_for, abort, render_template, flash
from contextlib import closing
# endregion

# region ------------------ CONFIGURATIONS -----------------------
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
SP_SERVER_PATH = 'http://192.168.2.191:8000'
HOST = '0.0.0.0'
PORT = 80
# endregion

# region ------------------ GLOBAL -----------------------
app = Flask(__name__)
data_base_manager = DataBaseManager("MainDB.db")
# endregion


# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        try:
            # find user in database
            username = request.form['username']
            password = request.form['password']
            query = "SELECT spID, spUserID FROM Users WHERE username='%s' AND passw='%s'" % (username, password)
            sp_id, sp_user_id = data_base_manager.exec_query(query)
            sp_url = get_sp_url(sp_id, sp_user_id)
            return redirect(sp_url)
        except:
            error = 'Invalid Credentials. Please try again.'
    return render_template('LoginMain.html', error=error)


@app.route('/login/<username> <password>')
def private_login(username, password):
    return 'Hello ' + username + ' ' + password + '!'
    #redirect to Service Provider
    #return redirect(('127.0.0.1', 80))


#@app.route('/connected/<user>')
#def connected(user):
#    return 'Hello %s, you are successfully connected.' % user


@app.route('/register/<id>', methods=['GET', 'POST'])
def register(id):
    print id
    error = None
    if request.method == 'POST':
        # add this user to database
        username = request.form['username']
        password = request.form['password']
        confirm_pass = request.form['confirmPassword']

        if confirm_pass == password:
            add_user(6, username, password, 1, id)
            return redirect(SP_SERVER_PATH+'/registeredas/'+id)
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('Register.html', error=error)


def get_sp_url(sp_id, sp_user_id):
    query = "SELECT redirectPath FROM SPs WHERE SPID=%d" % sp_id
    try:
        #path = data_base_manager.exec_query(query)
        return '%s/user/%d' % (SP_SERVER_PATH, sp_user_id)
    except:
        pass


def add_user(id, username, passw, sp_id, sp_user_id):
    fields = [(id, username, passw, sp_id, sp_user_id)]
    data_base_manager.insert("Users", fields)
    data_base_manager.print_table("Users")


def create_db():
    fields = ["ID integer primary key autoincrement", "username text not null", "passw text not null",
              "spID int not null", "spUserID int not null"]
    data_base_manager.create_table("Users", fields)
    fields = [(1, 'elle', 'EL', 1, 11), (2, 'David', '2511', 1, 22), (3, 'dana123', '12345', 1, 33),
              (4, 'dana123', '12345', 2, 11), (5, 'elle', 'EL', 2, 22)]
    data_base_manager.insert("Users", fields)
    data_base_manager.print_table("Users")

    fields = ["SPID integer primary key autoincrement", "details text not null", "redirectPath text not null",
              "key text not null"]
    data_base_manager.create_table("SPs", fields)
    fields = [(1, 'Sp1...', 'http://192.168.2.191', 'key1'), (2, 'Sp2...', 'http:/...', 'key2')]
    data_base_manager.insert("SPs", fields)
    data_base_manager.print_table("SPs")


def main():
    #create_db()
    app.run(host=HOST, port=PORT)
    #app.run(host='0.0.0.0', port=80)

if __name__ == '__main__':
    main()