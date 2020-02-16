#server.py
import socket
host=''
port=12345
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#AF_INET means that this is an internet socket
#SOCK_STREAM means we use a TCP socket
s.bind((host, port))
print('socket binded to', port)
backlog = 5
# backlog = number of queued connections
s.listen(backlog)
#listen for connections
conn,addr=s.accept()
print('socket is listening')
print('got connection from',addr)
#conn is a new socket object usable to send and recieve data on connection
#addr is address bound to socket on other end of connection
while 1:
    name = input('Hello, say something to the client')
    print('waiting for client\'s response')
    conn.send(name.encode())
    data=conn.recv(1024).decode('utf-8')
    print('recieved from client address: ', addr)
    print('Message recieved: ',data)
    #socket.send is teh data sent to client
    #socket has to be byte connected to remote socket
    #returns number of bytes sent
conn.close()
#closes connection
