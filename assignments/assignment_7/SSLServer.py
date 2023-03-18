import socket
from socket import AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import ssl

def handle_client(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        response = data.decode().upper().encode()
        conn.sendall(response)

def main():
    server_ip = "localhost"
    server_port = 8443

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="example.crt", keyfile="example.key")

    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)

    print("Server listening on {}:{}".format(server_ip, server_port))

    while True:
        client_socket, client_addr = server_socket.accept()
        print("Connection from:", client_addr)
        with context.wrap_socket(client_socket, server_side=True) as secure_sock:
            handle_client(secure_sock)
        print("Connection closed:", client_addr)

if __name__ == "__main__":
    main()