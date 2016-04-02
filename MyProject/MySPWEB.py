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
# endregion

# region ------------------ CONFIGURATIONS -----------------------
DEBUG = True
SECRET_KEY = 'other development key'
USERNAME = 'admin'
PASSWORD = 'default pass'
#MAIN_SERVER_PATH = 'http://192.168.2.193:80'
MAIN_SERVER_PATH = 'http://10.0.0.9:80'
HOST = '0.0.0.0'
PORT = 8000
# endregion

# region ------------------ GLOBAL -----------------------
app = Flask(__name__)
data_base_manager = DataBaseManager("PhoneBookDB.db")
key = b'Sixteen Byte Key'
e = Encryption(key)
# endregion


@app.route('/')
def index():
    return render_template('PhoneBookIndex.html')


# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username != 'admin' or password != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect('/login/%s %s' % (username, password))
    return render_template('LoginSP.html', error=error)


@app.route('/login/<server>')
def private_login(server):
    # redirect to My Main Server
    if server.lower() == "mymainserver":
        return redirect(MAIN_SERVER_PATH+'/login')  # /%s %s' % (username, password), code=302)


@app.route('/user/<userid>')
def profile(userid):
    # show user profile
    userid = e.decryptAES(userid)
    query = "SELECT name, age, phoneNum FROM UserProfiles WHERE ID=%s" % userid
    print query
    name, age, phone_num = data_base_manager.exec_query(query)
    if name:
        return render_template('Profile.html', name=name, age=age, phoneNum=phone_num)
    else:
        # error if userID was invalid
        pass


@app.route('/register')
def register():
    user_id = generate_user_id()
    user_id = str(user_id)
    user_id = e.encryptAES(user_id)
    return redirect(MAIN_SERVER_PATH+"/register/"+user_id)


@app.route('/registeredas/<user>', methods=['GET', 'POST'])
def registered(user):
    user = e.decryptAES(user)
    error = None
    if request.method == 'POST':
        # add this user to database
        name = request.form['name']
        age = request.form['age']
        phone_num = request.form['phoneNum']

        try:
            add_user(user, name, age, phone_num)
            user = e.encryptAES(user)
            return redirect('/user/'+user)
        except:
            error = 'Invalid Info. Please try again.'
    return render_template('RegisterToSP.html', error=error)


def generate_user_id():
    return 44


def add_user(id, name, age, phone_num):
    fields = [(id, name, age, phone_num)]
    data_base_manager.insert("UserProfiles", fields)
    data_base_manager.print_table("UserProfiles")


def create_db():
    fields = ["ID integer primary key autoincrement", "name text not null", "age integer not null",
              "phoneNum text not null"]
    data_base_manager.create_table("UserProfiles", fields)
    fields = [(101, 'Elizabeth', 17, '09-8656735'), (102, 'David', 10, '03-1234567'),
              (103, 'Dana', 25, '04-9182734')]
    data_base_manager.insert("UserProfiles", fields)
    data_base_manager.print_table("UserProfiles")


def main():
    create_db()
    app.run(host=HOST, port=PORT)

if __name__ == '__main__':
    main()