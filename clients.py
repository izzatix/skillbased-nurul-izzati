import socket

def get_user_input():
    server_ip = "izani.synology.me"
    port = 8443
    message = input("Enter your student ID: ")
    return server_ip, port, message

def send_message(server_ip, port, message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, port))
    client_socket.send(message.encode())
    reply = client_socket.recv(1024)
    print(f"Server reply: {reply.decode()}")
    client_socket.close()

if __name__ == "__main__":
    server_ip, port, message = get_user_input()
    send_message(server_ip, port, message)
