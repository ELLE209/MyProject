
# region ---------------------- IMPORTS -------------------------
from DataBaseManager import *
from Encryption import *
from ThreadWithReturnValue import *
import socket
from flask import Flask, request, redirect, render_template
import thread
import string
import random
# endregion

# region ------------------ CONFIGURATIONS ----------------------
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
HOST = '0.0.0.0'
PORT = 80
DB_NAME = "MainDB.db"
MASTER = b'Sixt33n Byt3 K3y'
# endregion


# region ---------------------- GLOBALS -------------------------
app = Flask(__name__)
server_sock = socket.socket()
# endregion


# region ------------------- URL_FUNCTIONS ----------------------
# route for handling the login page logic
@app.route('/login/<sp>', methods=['GET', 'POST'])
def login(sp):
    error = None
    if request.method == 'POST':
        try:
            # find user in database
            username = request.form['username']
            password = request.form['password']
            sp_id = int(sp)  # add decryption
            query = "SELECT spUserID FROM Users WHERE username='%s' AND passw='%s' AND spID=%d" %\
                    (username, password, sp_id)
            data_base_manager = DataBaseManager(DB_NAME)
            sp_user_id = data_base_manager.exec_query(query)[0]
            data_base_manager.close_connection()
            sp_user_id = get_encrypt_obj(sp_id).encryptAES(str(sp_user_id))
            sp_url = '%s/user/%s' % (get_sp_url(sp_id), str(sp_user_id))
            return redirect(sp_url)
        except Exception, ex:
            error = 'Invalid Credentials. Please try again.'
            print ex
    return render_template('LoginMain.html', error=error)


# route for handling the registration page logic
@app.route('/register/<userid> <sp>', methods=['GET', 'POST'])
def register(userid, sp):
    print userid
    print "sp:   " + sp
    sp_id = int(sp)
    sp_userid = get_encrypt_obj(sp_id).decryptAES(userid)
    error = None
    if request.method == 'POST':
        # add this user to database
        username = request.form['username']
        password = request.form['password']
        confirm_pass = request.form['confirmPassword']

        if confirm_pass == password:
            data_base_manager = DataBaseManager(DB_NAME)
            user_id = data_base_manager.last_id("Users") + 1
            data_base_manager.close_connection()
            add_user(user_id, username, password, sp_id, sp_userid)
            sp_userid = get_encrypt_obj(sp_id).encryptAES(sp_userid)
            return redirect(get_sp_url()+'/registeredas/'+sp_userid)
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('Register.html', error=error)
# endregion


# region ------------------ OTHER_FUNCTIONS ---------------------
def get_sp_url(sp_id=1):
    query = "SELECT redirectPath FROM SPs WHERE SPID=%d" % sp_id
    try:
        data_base_manager = DataBaseManager(DB_NAME)
        path = data_base_manager.exec_query(query)[0]
        data_base_manager.close_connection()
        return path
    except Exception, e:
        print 'Unable to execute query: ' + query
        print e


def get_encrypt_obj(sid):
    query = "SELECT key FROM SPs WHERE SPID=%d" % sid
    data_base_manager = DataBaseManager(DB_NAME)
    key = data_base_manager.exec_query(query)[0]
    data_base_manager.close_connection()
    key = Encryption(MASTER).decryptAES(key)
    return Encryption(key)


def add_user(id, username, passw, sp_id, sp_user_id):
    fields = [(id, username, passw, sp_id, sp_user_id)]
    data_base_manager = DataBaseManager(DB_NAME)
    data_base_manager.insert("Users", fields)
    data_base_manager.print_table("Users")
    data_base_manager.close_connection()


def create_db():
    data_base_manager = DataBaseManager(DB_NAME)
    fields = ["ID integer primary key autoincrement", "username text not null", "passw text not null",
              "spID integer not null", "spUserID integer not null"]
    data_base_manager.create_table("Users", fields)

    fields = ["SPID integer primary key autoincrement", "details text not null", "redirectPath text not null",
              "key text not null"]  # , "encryptObj blob not null"]
    data_base_manager.create_table("SPs", fields)
    data_base_manager.close_connection()


def generate_random(size=16):
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    key = ''
    for i in range(size):
        key += random.choice(chars)
    return key


def sps_comm():
    while True:
        sp_sock, sp_addr = server_sock.accept()
        sp_thread = ThreadWithReturnValue(target=register_sp, args=(sp_sock,))
        sp_thread.start()
        fields = sp_thread.join()
        data_base_manager = DataBaseManager("MainDB.db")
        data_base_manager.insert("SPs", fields)
        data_base_manager.print_table("SPs")
        data_base_manager.close_connection()


def register_sp(sp_sock):
    try:
        sp_sock.send('OK Send name redirectpath')
        print 'OK Send name redirectpath'
        sp_info = sp_sock.recv(1024)
        print sp_info
        sp_name, sp_server_path = sp_info.split('@')
        new_id = 1
        key = generate_random()

        # change encryption to Asymmetric
        key2send = Encryption(b'Sixteen Byte Key').encryptAES(key)
        print key2send + '@' + str(new_id)
        sp_sock.send(key2send + '@' + str(new_id))

        ans = sp_sock.recv(1024)
        print ans
        if not ans.startswith('OK'):
            raise ValueError
        sp_sock.close()

        key = Encryption(MASTER).encryptAES(key)
        return [(new_id, sp_name, sp_server_path, key), ]

    except Exception, e:
        print "ERROR"
        print e
# endregion


# region ------------------------ MAIN --------------------------
def main():
    create_db()

    data_base_manager = DataBaseManager(DB_NAME)
    fields = [(1, 'elle', 'EL', 1, 101), (2, 'David', '2511', 1, 102), (3, 'dana123', '12345', 1, 103),
              (4, 'dana123', '12345', 2, 101), (5, 'elle', 'EL', 2, 102)]
    data_base_manager.insert("Users", fields)
    data_base_manager.print_table("Users")
    data_base_manager.print_table("SPs")
    data_base_manager.close_connection()

    server_sock.bind((HOST, int(PORT)+1))
    server_sock.listen(5)
    thread.start_new_thread(sps_comm, ())

    app.run(host=HOST, port=PORT)

if __name__ == '__main__':
    main()
# endregion
