import socket
import ssl

HOST = "localhost"
PORT = 8443
KEY_FILE = "example.key"
CERT_FILE = "example.crt"

def main():
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((HOST, PORT))
        sock.listen(5)

        print("Server is listening on", HOST, ":", PORT)

        while True:
            conn, addr = sock.accept()
            print("Client connected:", addr)
            conn_ssl = context.wrap_socket(conn, server_side=True)

            try:
                data = conn_ssl.recv(1024).decode("utf-8")
                while data:
                    print("Received:", data)
                    response = data.upper().encode("utf-8")
                    conn_ssl.sendall(response)
                    data = conn_ssl.recv(1024).decode("utf-8")
            finally:
                conn_ssl.shutdown(socket.SHUT_RDWR)
                conn_ssl.close()

if __name__ == "__main__":
    main()