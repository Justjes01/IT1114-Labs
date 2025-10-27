# Program Name: Assignment4A.py
# Course: IT3883/Section W01
# Student Name: Jessica Scales
# Assignment Number: Lab4
# Due Date: 10/26/2025
# Purpose: This program prompts the user for a string, sends it to Program B over a socket,
#          and prints the response received from Program B (converted to uppercase).
# Resources: Python documentation for socket module, lecture notes

import socket
import time

# Hardcoded server IP and port
SERVER_IP = "127.0.0.1"  # localhost
SERVER_PORT = 40001       # Port > 40000 to avoid conflicts
MAX_RETRIES = 5           # Number of times to retry connection
RETRY_DELAY = 1           # Seconds between retries

def main():
    user_message = input("Enter a message to send to Program B: ")

    # Create TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # Attempt to connect to server with retries
        for attempt in range(MAX_RETRIES):
            try:
                client_socket.connect((SERVER_IP, SERVER_PORT))
                print(f"Connected to server at {SERVER_IP}:{SERVER_PORT}")
                break
            except ConnectionRefusedError:
                print(f"Connection refused, retrying in {RETRY_DELAY} second(s)...")
                time.sleep(RETRY_DELAY)
        else:
            print("Failed to connect to the server. Make sure Program B is running.")
            return

        # Send the message
        client_socket.sendall(user_message.encode('utf-8'))

        # Receive the response
        response = client_socket.recv(1024)
        print("Received from Program B:", response.decode('utf-8'))

if __name__ == "__main__":
    main()