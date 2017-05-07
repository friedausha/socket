import socket
import sys
import struct
import binascii
try:
    clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print ('Failed to create socket. Error code: '+str(msg[0])+' , Error message : '+msg[1])
print ('Socket created')
host = raw_input("Enter the host IP : ")
#port = raw_input("Enter the host port : ")
server_address = (host, 887)
try:
    clientsock.connect(server_address)
except socket.error, msg:
    print('Error code : '+ str(msg[0]) + msg[1])
while True:
    op=raw_input("Enter an operand : ")
    if op == 'STOP':
        print>>sys.stderr, 'Closing socket'
        clientsock.close()
        break
    elif op == '+' or op == '-' or op == '*' or op == '/' :
        clientsock.sendall(op)
        num1=(raw_input("Enter a number : "))
        clientsock.sendall(num1)
        num2=(raw_input("Enter a number : "))
        clientsock.sendall(num2)
        data=clientsock.recv(1024)
        print(data)
    else:
        print("Operand not found")
#finally:
#   print>>sys.stderr, 'Closing socket'
#   clientsock.close()


