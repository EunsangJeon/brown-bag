import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
# socket.socket() creates a socket object that supports the context manager type,
# so you can use it in a with statement.
# There’s no need to call s.close()
# (A context manager is an object that defines the runtime context to be established when executing a with statement)
# AF_INET is the Internet address family for IPv4.
# SOCK_STREAM is the socket type for TCP.

  s.bind((HOST, PORT))
  # note: The values passed to bind() depend on the address family.
  s.listen()
  # listen() enables a server to accept() connections. It makes it a “listening” socket.
  conn, addr = s.accept()
  # accept() blocks and waits for an incoming connection.
  # When a client connects, it returns a new socket object representing the connection
  # and a tuple holding the address of the client. 
  with conn:
    print('Connected by', addr)
    while True:
      data = conn.recv(1024) #1024 bytes
      if not data:
        break
      conn.sendall(data)
      # conn.recv() reads whatever data the client sends and echoes it back using conn.sendall().
