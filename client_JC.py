
import socket 
s = socket.socket()
host = '192.168.2.163' 
port = 5000      
s.connect((host, port))
print(s.recv(1024))
s.close()