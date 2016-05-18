import socket

s=socket.socket()
host=socket.gethostname()
port= 5111
s.connect((host,port))

print (s.recv(1024))
s.send(input('Enter your message::\n'))
print(s.recv(1024))
s.close
