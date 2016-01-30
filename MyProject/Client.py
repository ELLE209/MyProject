#####################   NOT NEEDED => DELETE CLIENT!   ################################
import socket
import sys


def connnect_to_sp(host, port):
    my_sock = socket.socket()
    my_sock.connect((host, port))
    return my_sock


def recv_msg(my_sock):
    data = my_sock.recv(1024)
    return data


def main(argv):
    my_sock = connnect_to_sp(argv[0], argv[1])

    #recv message
    data = recv_msg(my_sock)
    if data:
        print data
        ans = raw_input()
        #send...
    else:
        print "End of connection"
        sys.exit(0)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.stdout("Usage: Client.py <host> <port>\n"
                   "Specify the host and port of the server you would like to connect to")
        sys.exit(1)
    else:
        main(sys.argv[1:])