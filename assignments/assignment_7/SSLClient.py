import socket
import ssl

HOST = "localhost"
PORT = 8443
CERT_FILE = "example.crt"

def main():
    context = ssl.create_default_context(cafile=CERT_FILE, capath=".")
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
        conn = context.wrap_socket(sock, server_side=False, server_hostname=HOST)
        conn.connect((HOST, PORT))

        print("Cipher suite:", conn.cipher()[0])

        while True:
            message = input("Enter a message to send (type 'exit' to quit): ")
            if message.lower() == "exit":
                break

            conn.sendall(message.encode("utf-8"))
            data = conn.recv(1024)
            
            if not data:
                print("No data received.")
                break
            
            print("Received from server:", data.decode("utf-8"))
        
        # Close the SSL connection
        conn.close()

if __name__ == "__main__":
    main()