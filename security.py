import ssl
import socket

# Create a secure context for data transmission
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="path/to/certfile", keyfile="path/to/keyfile")

# Create a socket and wrap it with the secure context
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
secure_socket = context.wrap_socket(server_socket, server_side=True)

# Bind and listen
secure_socket.bind(('localhost', 8443))
secure_socket.listen(5)

print("Server listening on port 8443...")

while True:
    client_socket, addr = secure_socket.accept()
    print(f"Connection from {addr}")
    data = client_socket.recv(1024)
    print(f"Received: {data.decode()}")
    client_socket.close()
