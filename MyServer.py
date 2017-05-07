import socket
import sys
from thread import *
serversock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
#host = '127.0.0.1'
port = 887
print(host)
print(port)
try:
    serversock.bind((host,port))
except socket.error as msg:
    print ('Bind failed, error code : ' + str(msg[0]) + " "+ msg[1])
    sys.exit()
serversock.listen(5)
def clientthread(clientsock):
    while True:
        op = clientsock.recv(1024)
        if op == 'STOP':
            break
        else:
            num1 = clientsock.recv(1024)
            num2 = clientsock.recv(1024)
            ang1=float(num1)
            #print(ang1)
            ang2=float(num2)
            #print(ang2)
            reply = "%.2f" % calc(op, ang1, ang2)
            reply1 = str(reply)
            clientsock.send(reply1)
def calc(op, num1, num2):
    if op == '+':
        return (num1 + num2)
    elif op == '-':
        return(num1 - num2)
    elif op == '*':
        return (num1 * num2)
    elif op == '/':
        return (num1 / num2)
while True:
    try:
        clientsock, addr = serversock.accept()
    except socket.error as msg:
        print('Error code : '+str(msg[0]) +" "+ msg[1])
    print("Got a connection from " + addr[0] + str(addr[1]))
    start_new_thread(clientthread, (clientsock, ))
serversock.close()
