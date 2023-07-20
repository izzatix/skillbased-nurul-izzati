import socket

def bar_to_atmosphere(pressure):
    return pressure * 0.986923

def handle_client(client_socket):
    try:
        data = client_socket.recv(1024).decode().strip()
        pressure = float(data)
        atmosphere_standard = bar_to_atmosphere(pressure)
        client_socket.send(str(atmosphere_standard).encode())
    except ValueError:
        client_socket.send(b"Invalid input. Please provide a valid pressure value.")
    finally:
        client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("192.168.21.129", 8484))
    server_socket.listen(1)

    print("Server is listening...")

    while True:
        client_socket, client_addr = server_socket.accept()
        print(f"Connection from {client_addr}")
        handle_client(client_socket)

if __name__ == "__main__":
    start_server()

