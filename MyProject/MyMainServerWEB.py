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


# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        # find user in database
        username = request.form['username']
        password = request.form['password']
        query = "SELECT spUserID FROM Users WHERE username='%s' AND passw='%s'" % (username, password)
        sp_user_id = data_base_manager.exec_query(query)
        if sp_user_id:
            return redirect('connected/%s' % username)
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('Login.html', error=error)


@app.route('/login/<username> <password>')
def private_login(username, password):
    return 'Hello ' + username + ' ' + password + '!'
    #redirect to Service Provider
    #return redirect(('127.0.0.1', 80))

@app.route('/connected/<user>')
def connected(user):
    return 'Hello %s, you are successfully connected.' % user


def create_db():
    fields = ["ID integer primary key autoincrement", "username text not null", "passw text not null",
              "spID int not null", "spUserID int not null"]
    data_base_manager.create_table("Users", fields)
    fields = [(1, 'elle', '12345', 1, 11), (2, 'elle1', '12345', 1, 11), (3, 'elle2', '12345', 1, 11)]
    data_base_manager.insert("Users", fields)
    data_base_manager.print_table("Users")

    fields = ["SPID integer primary key autoincrement", "details text not null", "key text not null"]
    data_base_manager.create_table("SPs", fields)


def main():
    #create_db()
    app.run(host='127.0.0.1', port=80)

if __name__ == '__main__':
    main()