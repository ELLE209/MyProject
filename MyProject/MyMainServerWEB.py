# region ----------------------- ABOUT --------------------------
"""
################################################################
# Created By: Elizabeth Langerman                              #
# Date: 04/2016                                                #
# Name: Identity Provider (IDP) Server =Main Server            #
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
from ThreadWithReturnValue import *
from flask import Flask, request, redirect, render_template
from Crypto.PublicKey import RSA
import ConfigParser
import socket
import thread
import hashlib
import pickle
import sys
# endregion

# region ------------------ CONFIGURATIONS ----------------------
config = ConfigParser.ConfigParser()
config.readfp(open('main_config.cfg'))  # path to config file

try:
    # get constants from configurations file
    PORT = int(config.get('General', 'port'))
    DB_NAME = config.get('General', 'db_name')
except ConfigParser.NoSectionError or ConfigParser.NoOptionError, e:
    print e
    sys.exit(1)

HOST = '0.0.0.0'
MASTER = b'Sixt33n Byt3 K3y'
# endregion

# region ---------------------- GLOBALS -------------------------
app = Flask(__name__)
server_sock = socket.socket()
# endregion


# region ------------------- URL_FUNCTIONS ----------------------
# route for MyMainServer login page
@app.route('/login/<sp>', methods=['GET', 'POST'])
def login(sp):
    error = None
    if request.method == 'POST':
        try:
            # get username & password hash from html form
            username = request.form['username']
            hashed_pass = hashlib.sha1(request.form['password']).hexdigest()
            sp_id = int(sp)

            # find user in database
            query = "SELECT spUserID FROM Users WHERE username='%s' AND passw='%s' AND spID=%d" %\
                    (username, hashed_pass, sp_id)
            data_base_manager = DataBaseManager(DB_NAME)
            sp_user_id = data_base_manager.exec_query(query)[0]
            data_base_manager.close_connection()

            # redirect to user's profile page is SP
            sp_user_id = get_encrypt_obj(sp_id).encryptAES(str(sp_user_id))
            addr=get_sp_url(sp_id)
            sp_url = '%s/user/%s' % (addr, str(sp_user_id))
            server = "PhoneBook Server"
            return render_template('RedirectPage.html', path=sp_url, server=server, addr=addr)
            #return redirect(sp_url)

        except Exception, exc:
            # if user wasn't found
            error = 'Invalid Credentials. Please try again.'
            print exc
    return render_template('LoginMain.html', error=error)


# route for registration page
@app.route('/register/<userid> <sp>', methods=['GET', 'POST'])
def register(userid, sp):
    print userid
    print "sp:   " + sp
    sp_id = int(sp)

    # decrypt user ID with the key for this SP
    sp_userid = get_encrypt_obj(sp_id).decryptAES(userid)

    error = None
    if request.method == 'POST':
        # get username & password hashes from html form
        username = request.form['username']
        password = hashlib.sha1(request.form['password']).hexdigest()
        confirm_pass = hashlib.sha1(request.form['confirmPassword']).hexdigest()

        if confirm_pass == password:
            # add this user to database
            data_base_manager = DataBaseManager(DB_NAME)
            user_id = data_base_manager.last_id("Users") + 1
            data_base_manager.close_connection()
            add_user(user_id, username, password, sp_id, sp_userid)

            # redirect to SP to continue registration
            sp_userid = get_encrypt_obj(sp_id).encryptAES(sp_userid)
            addr = get_sp_url(sp_id)
            path = addr + '/registeredas/' + sp_userid
            server = "PhoneBook Server"
            return render_template('RedirectPage.html', path=path, server=server, addr=addr)
            #return redirect()

        else:
            # if password confirmation was incorrect
            error = 'Invalid Credentials. Please try again.'
    return render_template('Register.html', error=error)
# endregion


# region ------------------ OTHER_FUNCTIONS ---------------------
# get SP url from db (for redirect)
def get_sp_url(sp_id=1):
    """
    Gets RedirectPath data from SPs table in db, for a specific SP
    :param sp_id: SP to find url of
    :return: path of this SP
    """
    query = "SELECT redirectPath FROM SPs WHERE SPID=%d" % sp_id
    try:
        data_base_manager = DataBaseManager(DB_NAME)
        path = data_base_manager.exec_query(query)[0]
        data_base_manager.close_connection()
        return path

    except Exception, e:
        print 'Unable to execute query: ' + query
        print e


# get encryption object for specific SP
def get_encrypt_obj(sid):
    """
    Gets encryption key from SPs table in db.
    Creates an instance of Encryption using that key.
    :param sid: SP server ID
    :return: AES encryption object
    """
    query = "SELECT key FROM SPs WHERE SPID=%d" % sid
    data_base_manager = DataBaseManager(DB_NAME)
    key = data_base_manager.exec_query(query)[0]
    data_base_manager.close_connection()
    key = Encryption(MASTER).decryptAES(key)
    return Encryption(key)


# add user to UserProfiles table in db
def add_user(id, username, passw, sp_id, sp_user_id):
    """
    Adds A row in UserProfiles table for a new user with this info:
    :param id: user ID
    :param username: chosen username
    :param passw: chosen password
    :param sp_id: ID of SP server to which the user is registrating
    :param sp_user_id: ID o this user in SP server
    :return: None
    """
    fields = [(id, username, passw, sp_id, sp_user_id)]
    data_base_manager = DataBaseManager(DB_NAME)
    data_base_manager.insert("Users", fields)
    data_base_manager.print_table("Users")
    data_base_manager.close_connection()


# create tables for DB
def create_db():
    # create Users table
    data_base_manager = DataBaseManager(DB_NAME)
    fields = ["ID integer primary key autoincrement", "username text not null", "passw text not null",
              "spID integer not null", "spUserID integer not null"]
    data_base_manager.create_table("Users", fields)

    # create SPs table
    fields = ["SPID integer primary key autoincrement", "details text not null", "redirectPath text not null",
              "key text not null"]
    data_base_manager.create_table("SPs", fields)
    data_base_manager.close_connection()


# generates public and private key
def generate_RSA_key():
    new_key = RSA.generate(2048)
    public = new_key.publickey()
    return public, new_key


# socket communication with new SPs
def sps_comm():
    """
    Server side of socket comm.
    Inserts newly connected SPs to DB.
    :return: None
    """
    public_key, new_key = generate_RSA_key()
    while True:
        sp_sock, sp_addr = server_sock.accept()
        sp_thread = ThreadWithReturnValue(target=register_sp, args=(sp_sock, public_key, new_key))
        sp_thread.start()
        fields = sp_thread.join()
        data_base_manager = DataBaseManager("MainDB.db")
        data_base_manager.insert("SPs", fields)
        data_base_manager.print_table("SPs")
        data_base_manager.close_connection()


# exchange details to register new SP, with socket
def register_sp(sp_sock, public_key, new_key):
    """
    Exchange of details between servers:
    Receives SP address, sends public key, ID for the new SP and receives encrypted symmetric key.
    :param sp_sock: Client socket of SP
    :param public_key: RSA public key to send
    :param new_key: the RSA key object
    :return: Details of newly registered SP
    """
    try:
        sp_sock.send('OK Send name redirectpath')
        print 'OK Send name redirectpath'

        # receive SP address
        sp_info = sp_sock.recv(1024)
        print sp_info
        sp_name, sp_server_path = sp_info.split('@')
        new_id = 1

        # send public key and ID
        print pickle.dumps(public_key) + '@' + str(new_id)
        sp_sock.send(pickle.dumps(public_key) + '@' + str(new_id))

        # receive symmetric key
        ans = sp_sock.recv(1024)
        ans = pickle.loads(ans)
        print ans
        symm_key = new_key.decrypt(ans)
        sp_sock.close()

        key = Encryption(MASTER).encryptAES(symm_key)
        return [(new_id, sp_name, sp_server_path, key), ]

    except Exception, e:
        print "ERROR"
        print e


# Insert a few rows to Users table in db
def insert_init_values():
    data_base_manager = DataBaseManager(DB_NAME)
    fields = [(1, 'elle', hashlib.sha1('EL').hexdigest(), 1, 101), (2, 'David', hashlib.sha1('2511').hexdigest(), 1, 102),
              (3, 'dana123', hashlib.sha1('12345').hexdigest(), 1, 103), (4, 'dana123', hashlib.sha1('12345').hexdigest(), 2, 101),
              (5, 'elle', hashlib.sha1('EL').hexdigest(), 2, 102)]
    data_base_manager.insert("Users", fields)

    # print db tables
    data_base_manager.print_table("Users")
    data_base_manager.print_table("SPs")

    data_base_manager.close_connection()
# endregion


# region ------------------------ MAIN --------------------------
def main():
    create_db()
    insert_init_values()

    # create server socket listener (communication itself in new thread)
    server_sock.bind((HOST, int(PORT)+1))
    server_sock.listen(5)
    thread.start_new_thread(sps_comm, ())

    app.run(host=HOST, port=PORT)

if __name__ == '__main__':
    main()
# endregion
