import socket
import threading
import random

QUOTES = [
    "If you want to love others, I think you should love yourself first. - BTS Kim Namjoon",
    "When something is delicious, it's zero calories. - BTS Kim Seokjin",
    "Life is tough, and things don't always work out well, but we should be brave and go on with our lives - BTS Min Yoongi",
    "When things get tough, look at the people who love you! You will get energy from them. - BTS Jung Hoseok",
    "Even if you feel that you are alone, don't throw yourself away. - BTS Park Jimin",
    "Challenge yourself! No matter how many times you fall, don't give up -BTS Kim Taehyung",
    "Life isn't about being perfect, it's about accomplishing your dream -BTS Jeon Jungkook",
    "WE PURPLE<3 YOU - BTS "
]

def handle_client(client_socket):
    quote = random.choice(QUOTES)
    client_socket.send(quote.encode())
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("192.168.21.129", 8888))
    server_socket.listen(5)

    print("QOTD Server is listening...")

    while True:
        client_socket, client_addr = server_socket.accept()
        print(f"Connection from {client_addr}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_server()

