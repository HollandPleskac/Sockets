'''Sockets 04: Mini-Project (Web Server)
-------------------------------------------------------------------------------
Creating a Web Server
 * Code creates a socket object and opens it on port 1234. Client sockets
    can "plug in" to port 1234 on the server. The lines.listen(10) tells Python
    to 'listen' for client sockets on port 1234.
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",1234))
s.listen(10)
 * Code waits until a client socket (Web Browser) connects.  Then, the code
     prints out the name (address) of the web browser that connected.
while True:
    browser,browser_address=s.accept()
    print("Browser connected at address: {}".format(browser_address))
 * Type : http://localhost:1234 in a Web Browser.  The browser will show an
     empty page, but the progam will print out something like:
     Browser connected at address: (127.0e.0.1,55158).  The program can accept
     socket connections from clients.
 * Code recieves the browser's message one letter at  a time, until it sees a
     'newline' character (indicating the end of the message). Then the program
     prints the message. Now running the program will additionally print:
     Message from browser: GET \ HTTP\1.1
ch=None
message=""
    while message[len(message)-2:]!='\r\n':
        ch=browser.recv(1).decode('utf-8')
        message=message+ch
    print("Message from browser: "+message)
 * The message we are recieving from the browser is an HTTP GET request.  We are
     the server and we are recieving the HTTP GET request.  Upon recieving this
     request, our program should send back an HTML webpage along with an
     HTTP/1.1 200 OK\r\n status code
browser.sendall(b"""HTTP/1.1 200 OK\r\n
<!DOCTYPE html>
<html>
    <head>
        <title>
        Python Web Server
        <\title>
        <h1>
        Python Web Server
        <\h1>
    <\head>
    <body>
        <p2>A Python web server is serving this webpage.<\p>
    <\body>
<\html>
        """)
browser.close()
-------------------------------------------------------------------------------
'''
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",80))
s.listen(5)
while True:
    browser,browser_address=s.accept()
    print("Browser connected at address: {}".format(browser_address))
    ch=None
    message=""
    while message[len(message)-2:]!='\r\n':
        ch=browser.recv(1).decode('utf-8')
        message=message+ch
    print("Message from browser: "+message)
    browser.sendall(b"""HTTP/1.1 200 OK\r\n
    <!DOCTYPE html>
    <html>
        <head><title>Python Web Server</title></head>
        <body>
            <h1>Python Web Server</h1>
            <p>A Python web server is serving this webpage.</p>
        </body>
    </html> """)
browser.close()
