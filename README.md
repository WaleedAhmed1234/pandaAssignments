'''
    Simple socket server using threads
'''

import socket
import sys
from thread import *

HOST = ''   # Symbolic name, meaning all available interfaces
PORT = 5111 # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')

#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print ('Socket bind complete')

#Start listening on socket
s.listen(10)
print ('Socket now listening')
def clientthread(conn,conn1):
    conn.send('Welcome to the server . Enter something and hit enter.\n')
    conn1.send('Welcome to the server . Enter something and hit enter.\n')
    while True:
        data = conn.recv(1024)
        conn1.send(data)
        data1 = conn1.recv(1024)
        conn.send(data1)
    conn.close()

#now keep talking with the client
while 1:

    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print ('Connected with ' + addr[0] + ':' + str(addr[1]))
    conn1, addr = s.accept()
    print ('Connected with ' + addr[0] + ':' + str(addr[1]))
    start_new_thread(clientthread,(conn,conn1))
s.close()
