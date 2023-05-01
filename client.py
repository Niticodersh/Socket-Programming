import socket

# Define the main function
def main():
    # Set the host and port values for the server
    host = '127.0.0.1'
    port = 5011

    # Create a new client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the client socket to the server
    client_socket.connect((host, port))

    try:
        while True:
            try:
                # Get user input for an arithmetic expression
                expression = input('Enter an arithmetic expression (e.g. "1 + 2"): ')
                if not expression:
                    break

                # Send the expression to the server
                client_socket.send(expression.encode() + b'\n')

                # Receive the result from the server
                result = client_socket.recv(1024).decode().strip()

                # Print the result
                print(f'Result: {result}')

            except KeyboardInterrupt:
                # Close the connection if the user interrupts the program
                print('Connection closed by keyboard interrupt')
                client_socket.close()
                break

    finally:
        # Close the client socket
        client_socket.close()

# Execute the main function if the script is run directly
if __name__ == '__main__':
    main()
