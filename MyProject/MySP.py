import socket
import sys

HOST_GUI = "127.0.0.1"
PORT_GUI = 5555

HOST_MAIN = "127.0.0.1"
PORT_MAIN = 7777

ID_DICT = {11: 1101,
           22: 2202,
           33: 3303,
           44: 4404}

INFO_DICT = {1101: ["Elizabeth", "054-2336641", "pink"],
             2202: ["Juliette", "052-1234567", "yellow"],
             3303: ["Daniel", "050-7654321", "green"],
             4404: ["David", "058-7372775", "blue"]}


def create_socket(addr):
    sock = socket.socket()
    sock.connect(addr)
    return sock


def get_user_info(main_id):
    if main_id in ID_DICT.keys():
        sp_id = ID_DICT[main_id]
        info_list = INFO_DICT[sp_id]
        info_str = ' '.join(info_list)
        return info_str
    else:
        return "0"


def main():
    gui_sock = create_socket((HOST_GUI, PORT_GUI))
    idp = gui_sock.recv(1024)

    if idp != "MyMainServer":
        sys.stdout("Try again with MyMainServer")
        sys.exit(1)

    idp_sock = create_socket((HOST_MAIN, PORT_MAIN))
    main_id = idp_sock.recv(1024)
    main_id = int(main_id)
    #main_id = 11

    user_info = get_user_info(main_id)
    gui_sock.send(user_info)

    gui_sock.close()
    idp_sock.close()


if __name__ == '__main__':
    main()