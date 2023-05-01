import socket

# Set the host IP address and port number
HOST = '127.0.0.1'  # Localhost
PORT = 5010    # Arbitrary port number

# Create a socket object using IPv4 addressing and TCP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
s.bind((HOST, PORT))
print("Bind to port",PORT)

# Listen for incoming connections
# Limit to only one client at a time
s.listen(1)

# Loop to keep the server running indefinitely
while True:
    # Wait for a client to connect
    conn, addr = s.accept()
    print(f'Connected to {addr}')

    # Connection established, handle requests from the client
    while True:
        # Receive data from the client
        data = conn.recv(1024).decode()
        print("Client:", data)

        # If no data received, client has closed the connection
        if not data:
            break

        # Process the request from the client
        try:
            # Evaluate the expression and get the result
            result = eval(data)

            # Send the result back to the client
            conn.sendall(str(result).encode())
            print("Server:", result)

        except Exception:
            # Send an error message back to the client
            conn.sendall(str("Invalid input").encode())

    # Close the connection with the client
    conn.close()
    print(f"Connection closed with {addr}")
