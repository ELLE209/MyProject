# region ----------------------- ABOUT --------------------------
"""
################################################################
# Created By: Elizabeth Langerman                              #
# Date: 04/2016                                                #
# Name: Srvice Provider (SP) Server for example                #
# Version: 1.0                                                 #
# Windows Tested Versions: Win 8 32-bit, Win 7 32-bit          #
# Python Tested Versions: 2.7 32-bit                           #
# Python Environment: PyCharm                                  #
################################################################
"""
# endregion

# region ---------------------- IMPORTS -------------------------
from DataBaseManager import *
from Encryption import *
from flask import Flask, request, redirect, render_template
import ConfigParser
import socket
#import netifaces
import sys
# endregion

# region ------------------ CONFIGURATIONS ----------------------
config = ConfigParser.ConfigParser()
config.readfp(open('sp_config.cfg'))

try:
    MY_IP = config.get('General', 'my_ip')
    PORT = int(config.get('General', 'port'))
    MAIN_SERVER_IP = config.get('General', 'MainServerIP')
    MAIN_SERVER_PORT = int(config.get('General', 'MainServerPort'))
    DB_NAME = config.get('General', 'db_name')
except ConfigParser.NoSectionError or ConfigParser.NoOptionError, e:
    print e
    sys.exit(1)

HOST = '0.0.0.0'
MAIN_SERVER_PATH = 'http://' + MAIN_SERVER_IP + ':' + str(MAIN_SERVER_PORT)
ME = 'PhoneBook' + '@' + 'http://' + MY_IP + ':' + str(PORT)
# endregion

# region ---------------------- GLOBALS -------------------------
app = Flask(__name__)
data_base_manager = DataBaseManager(DB_NAME)
# endregion


# region ------------------- URL_FUNCTIONS ----------------------
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
        return redirect(MAIN_SERVER_PATH + '/login/' + str(my_sp_id))


@app.route('/user/<userid>')
def profile(userid):
    # show user profile
    try:
        userid = enc_obj.decryptAES(userid)
    except Exception, e:
        print e
    query = "SELECT name, age, phoneNum FROM UserProfiles WHERE ID=%s" % userid
    name, age, phone_num = data_base_manager.exec_query(query)
    if name:
        return render_template('Profile.html', name=name, age=age, phoneNum=phone_num)
    else:
        # error if userID was invalid
        pass


@app.route('/register')
def register():
    user_id = data_base_manager.last_id("UserProfiles") + 1
    user_id = str(user_id)
    user_id = enc_obj.encryptAES(user_id)
    return redirect(MAIN_SERVER_PATH+"/register/"+user_id + " " + str(my_sp_id))


@app.route('/registeredas/<user>', methods=['GET', 'POST'])
def registered(user):
    user = enc_obj.decryptAES(user)
    error = None
    if request.method == 'POST':
        # add this user to database
        name = request.form['name']
        age = request.form['age']
        phone_num = request.form['phoneNum']

        try:
            add_user(user, name, age, phone_num)
            user = enc_obj.encryptAES(user)
            return redirect('/user/'+user)
        except:
            error = 'Invalid Info. Please try again.'
    return render_template('RegisterToSP.html', error=error)
# endregion


# region ------------------ OTHER_FUNCTIONS ---------------------
def add_user(id, name, age, phone_num):
    fields = [(id, name, age, phone_num)]
    data_base_manager.insert("UserProfiles", fields)
    #data_base_manager.print_table("UserProfiles")


def create_db():
    fields = ["ID integer primary key autoincrement", "name text not null", "age integer not null",
              "phoneNum text not null"]
    data_base_manager.create_table("UserProfiles", fields)
    fields = [(101, 'Elizabeth', 17, '09-8656735'), (102, 'David', 10, '03-1234567'),
              (103, 'Dana', 25, '04-9182734')]
    data_base_manager.insert("UserProfiles", fields)
    #data_base_manager.print_table("UserProfiles")


def save_key_id(key, my_id):
    key = Encryption(b'Sixteen Byte Key').decryptAES(key)
    enc = Encryption(key)  # correct enc_obj: use to encrypt & decrypt sent data
    my_id = int(my_id)  # send it for sp identification in redirect
    return enc, my_id


def connect_mymainserver():
    my_sock = socket.socket()
    my_sock.connect((MAIN_SERVER_IP, MAIN_SERVER_PORT+1))
    ans = my_sock.recv(1024)
    print ans
    try:
        if not ans.startswith('OK'):
            raise ValueError
        print ME
        my_sock.send(ME)
        data = my_sock.recv(1024)
        key, my_id = data.split('@')
        my_sock.send('OK End Connection')
        my_sock.close()
        return save_key_id(key, my_id)
    except Exception:
        my_sock.send('Error')
        my_sock.close()
# endregion


# region ------------------------ MAIN --------------------------
create_db()
enc_obj, my_sp_id = connect_mymainserver()


def main():
    app.run(host=HOST, port=PORT)
    data_base_manager.close_connection()

if __name__ == '__main__':
    main()
# endregion
