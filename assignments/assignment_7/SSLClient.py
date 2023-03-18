import socket
import ssl
import sys
import random
import string

def main():
    server_ip = "localhost"
    server_port = 8443

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile="example.crt")
    context.load_verify_locations(capath=".")

    ssl_sock = context.wrap_socket(sock, server_hostname=server_ip)
    ssl_sock.connect((server_ip, server_port))

    print("Negotiated Cipher Suite: ", ssl_sock.cipher())

    test_data = "".join([random.choice(string.ascii_lowercase) for i in range(15)]) + "\n"
    ssl_sock.sendall(test_data.encode("utf-8"))

    response = ssl_sock.recv(1024)
    print("Received from server: ", response.decode("utf-8"))

    ssl_sock.close()

if __name__ == "__main__":
    main()
