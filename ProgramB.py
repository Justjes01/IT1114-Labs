# Program Name: Assignment4B.py
# Course: IT3883/Section W01
# Student Name: Jessica Scales
# Assignment Number: Lab4
# Due Date: 10/26/2025
# Purpose: This program listens for a message from Program A, converts it to uppercase,
#          and sends it back to Program A.
# Resources: Python documentation for socket module, lecture notes

import socket

# Hardcoded IP and port (must match Program A)
HOST = "127.0.0.1"
PORT = 40001

def main():
    # Create TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Bind socket and start listening
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"Server listening on {HOST}:{PORT}")

        # Accept connection from client
        connection, client_address = server_socket.accept()
        with connection:
            print(f"Connected by {client_address}")

            # Receive message from client
            data = connection.recv(1024)
            if data:
                received_message = data.decode('utf-8')
                print("Received from Program A:", received_message)

                # Convert letters to uppercase
                response_message = received_message.upper()

                # Send back to client
                connection.sendall(response_message.encode('utf-8'))
                print("Sent uppercase message back to Program A")

if __name__ == "__main__":
    main()