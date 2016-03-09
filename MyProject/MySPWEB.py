# region ------------------ ABOUT -----------------------
"""
My Project...
"""
# endregion

# region ------------------ IMPORTS -----------------------
from DataBaseManager import *

from flask import Flask, request, g, redirect, url_for, \
    abort, render_template, flash
from contextlib import closing
# endregion

# region ------------------ CONFIGURATIONS -----------------------
#DATABASE = 'C:\MyProject\MyProject\databases\MyDB.db'
#DATABASE = 'C:\Users\Elizabeth\Documents\GitHub\MyProject\MyProject\databases\MyDB.db'
DEBUG = True
SECRET_KEY = 'other development key'
USERNAME = 'admin'
PASSWORD = 'default pass'
MAIN_SERVER_PATH = 'http://10.0.0.9:80'
# endregion

# region ------------------ GLOBAL -----------------------
app = Flask(__name__)
data_base_manager = DataBaseManager("PhoneBookDB.db")
# endregion

#@app.route('/login')
#def login():
#    return 'Welcome to My Service Provider!'


# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('LoginSP.html', error=error)


@app.route('/login/<username> <password>')
def private_login(username, password):
    # return 'Hello ' + username + ' ' + password + '!'
    # redirect to My Main Server
    return redirect(MAIN_SERVER_PATH+'/login')  # /%s %s' % (username, password), code=302)


@app.route('/user/<userid>')
def profile(userid):
    # show user profile
    #query = "SELECT name, age, phoneNum FROM UserProfiles WHERE ID=11"
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
    return redirect(MAIN_SERVER_PATH+"/register")


@app.route('/registeredas/<user>')
def registered(user):
    error = None
    if request.method == 'POST':
        # add this user to database
        name = request.form['name']
        age = request.form['age']
        phone_num = request.form['phoneNum']

        if name and age and phone_num:
            add_user(44, name, age, phone_num)
            return redirect('/user/44')
        else:
            error = 'Invalid Info. Please try again.'
    return render_template('RegisterToSP.html', error=error)


def generate_user_id():
    return 44


def add_user(id, name, age, phone_num):
    fields = [(id, name, age, phone_num)]
    data_base_manager.insert("UserProfiles", fields)
    data_base_manager.print_table("UserProfiles")


def create_db():
    fields = ["ID integer primary key", "name text not null", "age int not null",
              "phoneNum text not null"]
    data_base_manager.create_table("UserProfiles", fields)
    fields = [(11, 'Elizabeth', 17, '09-8656735'), (22, 'David', 10, '03-1234567'),
              (33, 'Dana', 25, '04-9182734')]
    data_base_manager.insert("UserProfiles", fields)
    data_base_manager.print_table("UserProfiles")


def main():
    create_db()
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    main()