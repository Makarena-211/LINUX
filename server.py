import socket 

sock = socket.socket()
sock.bind(('', 9099))
sock.listen(1)
conn, addr = sock.accept()
print (addr)

data = conn.recv(1024)
print (data)

conn.close()
