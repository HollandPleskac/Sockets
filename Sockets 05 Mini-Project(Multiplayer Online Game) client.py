# run this code on a separate computer
#type inconfig into the terminal to get the ip address

import socket
host = '192.168.1.221' # server ip address
port = 12345
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
while 1:
    data = s.recv(1024)
    print('Revieved from server', repr(data))
s.close()
