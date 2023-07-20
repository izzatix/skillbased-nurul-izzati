import socket

def get_user_input():
    while True:
        try:
            pressure = float(input("Enter the pressure value in bar: "))
            return pressure
        except ValueError:
            print("Invalid input. Please enter a valid pressure value.")

def connect_to_server(pressure):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("192.168.21.129", 8484))
    client_socket.send(str(pressure).encode())

    atmosphere_standard = client_socket.recv(1024).decode()
    print(f"Received atmosphere-standard value from server: {atmosphere_standard} atm")

    client_socket.close()

if __name__ == "__main__":
    pressure = get_user_input()
    connect_to_server(pressure)

