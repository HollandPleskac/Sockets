#socket 03 mini-project(webpage downloader) review
from socket import *
connection = socket(AF_INET, SOCK_STREAM)
server_ip_address = gethostbyname('www.google.com')
server_port = 80
connection.connect((server_ip_address, server_port))
connection.sendall(b"GET / HTTP/1.1\r\n\r\n")
#command sends the server a requets for homepage(called /) of the website.
# /r/n/r/n is a 'line ending' that tells google.com that the message has ended
while True:
    recieved_letter = connection.recv(1).decode('utf-8')
    if recieved_letter == '':
        break
    print(recieved_letter,end='')
connection.close()
