import socket
import ssl

def main():
    server_ip = "localhost"
    server_port = 8443

    context = ssl.create_default_context(cafile="example.crt", capath=".")

    with socket.create_connection((server_ip, server_port)) as sock:
        with context.wrap_socket(sock, server_hostname=server_ip) as ssock:
            print("Connected using cipher suite:", ssock.cipher())
            while True:
                message = input("Enter a message to send (type 'exit' to quit): ")
                if message.lower() == "exit":
                    break
                ssock.sendall(message.encode())
                data = ssock.recv(1024)
                print("Received from server:", data.decode())

if __name__ == "__main__":
    main()
