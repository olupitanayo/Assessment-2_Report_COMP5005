import socket; import ssl; import json
def create_server():
    # This is to create a socket
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')
    # This is to create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sock.bind(('localhost', 12345))
    sock.listen(5)
    # This is to Wrap the socket with SSL
    secure_sock = context.wrap_socket(sock, server_side=True)
    return secure_sock
def handle_client(conn):
    try:
        data = conn.recv(1024)
        health_data = json.loads(data.decode())
        print('Received health data:', health_data)
        # Process and respond
        response_data = {"status": "received", "comment": "Data is secure and processed"}
        conn.send(json.dumps(response_data).encode())
    finally:
        conn.close()
if __name__ == "__main__":
    secure_sock = create_server()
    try:
        while True:
            conn, addr = secure_sock.accept()
            print('Connected by', addr)
            handle_client(conn)
    except KeyboardInterrupt:
        print("Server is shutting down.")
    finally:
        secure_sock.close()