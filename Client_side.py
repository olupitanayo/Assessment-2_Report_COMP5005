import socket; import ssl; import json
def create_client():
    # This depicts path to the self-signed certificate generated using SSL
    cert_path = r'C:\Users\opeye\PycharmProjects\pythonProject1\cert.pem'
    # This is configured to automatically use secure protocol version supported by both the client and the server.
    context = ssl.create_default_context()
    # This is to Load the self-signed certificate generated
    context.load_verify_locations(cert_path)
    # No need to state the SSL version as it will negotiate the best version
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname='localhost')
    conn.connect(('localhost', 12345))
    return conn
if __name__ == "__main__":
    conn = create_client()
    try:
        # Simulated Sensitive health data
        health_data = {"patient_id": 123, "heart_rate": 80, "blood_pressure": "120/80",
                       "Step_count": "3000"}
        conn.send(json.dumps(health_data).encode())
        response = conn.recv(1024)
        print('Server responded:', response.decode())
    finally:
        conn.close()
