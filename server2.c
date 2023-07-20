#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
#include <arpa/inet.h>

int main() {
    int server_socket, client_socket, random_number;
    struct sockaddr_in server_addr, client_addr;
    socklen_t client_addr_len = sizeof(client_addr);

    // Create socket
    server_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (server_socket < 0) {
        perror("Error in socket");
        exit(EXIT_FAILURE);
    }

    // Set server address
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(8443);
    server_addr.sin_addr.s_addr = INADDR_ANY;

    // Bind socket to the specified address and port
    if (bind(server_socket, (struct sockaddr *)&server_addr, sizeof(server_addr>
        perror("Error in bind");
        exit(EXIT_FAILURE);
    }

    // Listen for incoming connections
    listen(server_socket, 5);

    printf("Server is listening...\n");

    // Accept a client connection
    client_socket = accept(server_socket, (struct sockaddr *)&client_addr, &cli>
    if (client_socket < 0) {
        perror("Error in accept");
 exit(EXIT_FAILURE);
    }

    // Generate a random number between 100 and 999
    srand(time(NULL));
    random_number = rand() % 900 + 100;

    // Send the random number to the client
    send(client_socket, &random_number, sizeof(random_number), 0);

    printf("Random number sent to the client: %d\n", random_number);

    // Close the sockets
    close(client_socket);
    close(server_socket);

    return 0;
}



