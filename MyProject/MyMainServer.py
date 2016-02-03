from subprocess import Popen, PIPE
import threading
import socket
import os
#import subprocess

HOST_MAIN = "127.0.0.1"
PORT_MAIN = 7777

HOST_GUI = "127.0.0.1"
PORT_GUI = 3333

INSIDE_PATH = r'\Login_GUI\Login_GUI\bin\Debug\Login_GUI.exe'


class IdpService(threading.Thread):

    def __init__(self, client_sock, client_addr):
        threading.Thread.__init__(self)
        self.client_sock = client_sock
        self.client_addr = client_addr
        self.gui_sock = socket.socket()
        self.gui_sock.bind((HOST_GUI, PORT_GUI))
        self.gui_sock.listen(1)


    def start_gui_process(self):
        # start C# process (login window)

        my_gui = Popen(PATH, stdout=PIPE, stderr=PIPE)
        stdout, stderr = my_gui.communicate()


    def get_user_pass(self):
        # get username & password from GUI
        # return a list with both credentials

        client, addr = self.gui_sock.accept()
        user_pass = client.recv(1024)
        client.close()

        if user_pass:
            lst = user_pass.split('#', 1)
            return lst
        else:
            return None


    def identify_user(self, username, password):
        # check if a user with these credentials exists
        # return the user's ID (or else return None)
        if username == "elle" and password == "12345":
            return 11
        else:
            return None
        #return user_id

    def try_login(self, lst):
        if lst:
            username, password = lst[0], lst[1]
            user_id = self.identify_user(username, password)

            if user_id:
                self.client_sock.send(str(user_id))
            else:
                self.start_gui_process()
                lst = self.get_user_pass()
                self.try_login(lst)

        else:
            self.client_sock.send("0")


    def run(self):
        self.start_gui_process()
        lst = self.get_user_pass()

        print lst
        self.try_login(lst)
        # if lst:
        #     username, password = lst[0], lst[1]
        #     user_id = self.identify_user(username, password)
        #
        #     if user_id:
        #         self.client_sock.send(str(user_id))
        #     else:
        #         self.start_gui_process()
        #         lst = self.get_user_pass()
        #         self.try_login(lst)
        #
        # else:
        #     self.client_sock.send("0")

        self.client_sock.close()
        self.gui_sock.close()


class Login:

    def __init__(self):
        pass

    def run(self):
        #ask client for username & password

        #
        pass

def main():
    main_sock = socket.socket()
    main_sock.bind((HOST_MAIN, PORT_MAIN))
    main_sock.listen(5)
    while True:
        client_sock, addr = main_sock.accept()
        idps = IdpService(client_sock, addr)
        idps.start()

    main_sock.close()


if __name__ == '__main__':
    os.chdir("..")
    PATH = os.getcwd() + INSIDE_PATH
    print PATH
    main()