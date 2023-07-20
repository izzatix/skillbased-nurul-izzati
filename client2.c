#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

int main() {
    int client_socket, random_number;
    struct sockaddr_in server_addr;

    // Create socket
    client_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (client_socket < 0) {
        perror("Error in socket");
        exit(EXIT_FAILURE);
    }

    // Set server address
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(8443);
    inet_pton(AF_INET, "192.168.21.129", &server_addr.sin_addr);

    // Connect to the server
    if (connect(client_socket, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Error in connect");
        exit(EXIT_FAILURE);
    }

    // Receive the random number from the server
    recv(client_socket, &random_number, sizeof(random_number), 0);

    printf("Received random number from server: %d\n", random_number);

    // Close the socket
    close(client_socket);

    return 0;
}
