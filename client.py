import socket


sock = socket.socket()
sock.connect(('localhost', 9099)) 

msg= b'Hello, world!'
sock.send(msg)

sock.close()
