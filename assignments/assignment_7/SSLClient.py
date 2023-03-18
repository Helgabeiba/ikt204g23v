import socket
import ssl
import sys
import random
import string

def main():
    # The server IP address and port should be the local loopback interface localhost and the
    # port to contact the same as selected in Task 2.
    server_ip = "localhost"
    server_port = 8443

    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Load the certificate in the file example.crt
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH, cafile="example.crt")
    context.load_verify_locations(capath=".")

    # Wrap the socket with the SSL context
    ssl_sock = context.wrap_socket(sock, server_hostname=server_ip)

    # Connect to the server
    ssl_sock.connect((server_ip, server_port))

    # Print the negotiated cipher suite
    print("Negotiated Cipher Suite: ", ssl_sock.cipher())

    # Test communication: send a lowercase sentence, receive it in uppercase
    test_data = "".join([random.choice(string.ascii_lowercase) for i in range(15)]) + "\n"
    ssl_sock.sendall(test_data.encode("utf-8"))

    response = ssl_sock.recv(1024)
    print("Received from server: ", response.decode("utf-8"))

    # Close the SSL socket
    ssl_sock.close()

if __name__ == "__main__":
    main()