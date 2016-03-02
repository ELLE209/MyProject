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
#DATABASE = 'C:\MyProject\MyProject\databases\MyDB.db'
#DATABASE = 'C:\Users\Elizabeth\Documents\GitHub\MyProject\MyProject\databases\MyDB.db'
DEBUG = True
SECRET_KEY = 'other development key'
USERNAME = 'admin'
PASSWORD = 'default pass'
# endregion

app = Flask(__name__)


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
    return render_template('Login.html', error=error)


@app.route('/login/<username> <password>')
def private_login(username, password):
    #return 'Hello ' + username + ' ' + password + '!'
    #redirect to My Main Server
    return redirect('http://192.168.2.193:80/login')  # /%s %s' % (username, password), code=302)


def main():
    app.run(host='0.0.0.0',port=80)

if __name__ == '__main__':
    main()