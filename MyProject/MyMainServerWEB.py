# region ------------------ ABOUT -----------------------
"""
My Project...
"""
# endregion

# region ------------------ IMPORTS -----------------------
from DataBaseManager import *
from Encryption import *

from flask import Flask, request, g, redirect, url_for, abort, render_template, flash
from contextlib import closing
import pickle
# endregion

# region ------------------ CONFIGURATIONS -----------------------
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
SP_SERVER_PATH = 'http://192.168.2.193:8000'
#SP_SERVER_PATH = 'http://10.0.0.9:8000'
HOST = '0.0.0.0'
PORT = 80
# endregion

# region ------------------ GLOBAL -----------------------
app = Flask(__name__)
data_base_manager = DataBaseManager("MainDB.db")
#key = b'Sixteen byte key'
#e = Encryption(key)
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
            print sp_user_id
            e = get_encrypt_obj(1)  # insert real spID
            sp_user_id = e.encryptAES(str(sp_user_id))
            print sp_user_id
            sp_url = get_sp_url(sp_id, sp_user_id)
            return redirect(sp_url)
        except:
            error = 'Invalid Credentials. Please try again.'
    return render_template('LoginMain.html', error=error)


# route for handling the registration page logic
@app.route('/register/<userid>', methods=['GET', 'POST'])
def register(userid):
    print userid
    e = get_encrypt_obj(1)  # insert real spID
    userid = e.decryptAES(userid)
    error = None
    if request.method == 'POST':
        # add this user to database
        username = request.form['username']
        password = request.form['password']
        confirm_pass = request.form['confirmPassword']

        if confirm_pass == password:
            add_user(6, username, password, 1, userid)
            userid = e.encryptAES(userid)
            return redirect(SP_SERVER_PATH+'/registeredas/'+userid)
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('Register.html', error=error)


def get_sp_url(sp_id, sp_user_id):
    query = "SELECT redirectPath FROM SPs WHERE SPID=%d" % sp_id
    try:
        #path = data_base_manager.exec_query(query)
        return '%s/user/%s' % (SP_SERVER_PATH, sp_user_id)
    except:
        pass


def get_encrypt_obj(sid):
    #query = "SELECT encryptObj FROM Users WHERE SPID=%d" % sid
    query = "SELECT key FROM SPs WHERE SPID=%d" % sid
    print query
    #e = data_base_manager.exec_query(query)
    key = data_base_manager.exec_query(query)[0]
    return Encryption(key)


def add_user(id, username, passw, sp_id, sp_user_id):
    fields = [(id, username, passw, sp_id, sp_user_id)]
    data_base_manager.insert("Users", fields)
    data_base_manager.print_table("Users")


def create_db():
    fields = ["ID integer primary key autoincrement", "username text not null", "passw text not null",
              "spID integer not null", "spUserID integer not null"]
    data_base_manager.create_table("Users", fields)

    fields = ["SPID integer primary key autoincrement", "details text not null", "redirectPath text not null",
              "key text not null"]  # , "encryptObj blob not null"]
    data_base_manager.create_table("SPs", fields)


def create_db2():
    fields = ["ID integer primary key autoincrement", "username text not null", "passw text not null",
              "spID integer not null", "spUserID integer not null"]
    data_base_manager.create_table("Users", fields)
    fields = [(1, 'elle', 'EL', 1, 101), (2, 'David', '2511', 1, 102), (3, 'dana123', '12345', 1, 103),
              (4, 'dana123', '12345', 2, 101), (5, 'elle', 'EL', 2, 102)]
    data_base_manager.insert("Users", fields)
    data_base_manager.print_table("Users")

    fields = ["SPID integer primary key autoincrement", "details text not null", "redirectPath text not null",
              "key text not null"]  # , "encryptObj blob not null"]
    data_base_manager.create_table("SPs", fields)
    key1 = b'Sixteen Byte Key'
    # 4th parameter: Encryption(key1)
    fields = [(1, 'Sp1...', 'http://192.168.2.191', key1), (2, 'Sp2...', 'http:/...', 'key2')]
    data_base_manager.insert("SPs", fields)
    data_base_manager.print_table("SPs")


def main():
    create_db()
    key1 = b'Sixteen Byte Key'
    # 4th parameter: Encryption(key1)
    fields = [(1, 'Sp1...', 'http://192.168.2.191', key1), (2, 'Sp2...', 'http:/...', 'key2')]
    data_base_manager.insert("SPs", fields)
    data_base_manager.print_table("SPs")
    #ConnectServers()
    #key = b'Sixteen byte key'
    #e = Encryption(key)
    app.run(host=HOST, port=PORT)

if __name__ == '__main__':
    main()