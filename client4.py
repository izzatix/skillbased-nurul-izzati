import socket

def get_quote_from_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("192.168.21.129", 8888))
    quote = client_socket.recv(1024).decode()
    print("Random Quote of the Day:")
    print(quote)
    client_socket.close()

if __name__ == "__main__":
    get_quote_from_server()





