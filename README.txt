server1.py
----------------------------------------------------------------------------------------------
# How server1.py code is working 
The code (server1.py) sets up a basic server that listens on a specific IP address and port number for incoming connections from clients. Here are the steps followed in the code:

The IP address and port number are defined at the beginning of the code.

A socket object is created with IPv4 addressing and TCP protocol.

The socket is bound to the specific IP address and port number defined earlier.

The server is set to listen for incoming connections. In this case, only one client connection is allowed at a time.

A while loop is used to keep the server running indefinitely. Within this loop, the server waits for a client to connect using the accept() method.

Once a client connects, the server receives data from the client using the recv() method.

The server processes the data received from the client by evaluating the expression using the eval() function.

If the evaluation is successful, the server sends the result back to the client using the sendall() method.

If the evaluation fails due to invalid input, the server sends an error message back to the client.

The server continues to receive and process data from the client until the client closes the connection.

When the client closes the connection, the server closes the connection with the client and prints a message indicating that the connection has been closed.

The server continues to listen for incoming connections and handle requests from clients.
---------------------------------------------------------------------------------------------------
# How to implement/execute this code -->

To execute this code on any Python framework like Jupiter Notebook, you can follow these steps:

Open your Python IDE or Jupiter Notebook.

Create a new Python file and copy-paste the code into the file.

Save the file with a suitable name, for example, "server1.py".

Run the Python file to start the server.

In a separate console or Jupiter Notebook cell, you can create a client program to connect to the server by creating a new Python file and copying the code for the client program.

Save the file with a suitable name, for example, "client.py".

Run the client program to connect to the server and send requests to it.

Note: If you are running the server and client on the same machine, you can use 'localhost' or '127.0.0.1' as the server address. If the server is running on a remote machine, you will need to use the IP address or hostname of the machine running the server. 


-------------------------------------------------------------------------------------------------
# Testcases 
all the test cases passed for the server1.py file. 
we evaluate it on 2 operands , 3 operands and even more it is working correctly. (with all operators like +,-,/,* in a expression.)

______________________________________________________________________________________________________________________________________________________________________________________________
server2.py
# how to compile this file on a python supported framework.
To run this code on any Python framework, you can follow these steps:

Save the code in a file with a .py extension, for example, "server2.py".

Open a terminal or command prompt and navigate to the directory where the file is located.

Run the command python server.py to start the server.

The server will start running and listening for incoming connections on the specified IP address and port number.

Clients can connect to the server using a socket connection and send expressions to be evaluated.

The server will evaluate the expression, send the result back to the client, and then close the connection.

To stop the server, you can press Ctrl-C in the terminal or command prompt.

Note: Before running the code, make sure that you have the required modules (socket, threading, re, and queue) installed. You can install them using the pip package manager.

---------------------------------------------------------------------------------------------------
# steps followed in the server2.py file -->
Import the necessary modules: socket, threading, re, and queue.

Define a function handle_client that takes in client_socket and client_address as arguments.

In the handle_client function, create a while loop that continuously receives data from the client using client_socket.recv(1024).

If there is no data received, break out of the loop.

Decode the received data using data.decode(), and remove any whitespace using strip().

Evaluate the expression using eval(expression), and store the result in the result variable.

If the result is not None, create a response string that includes the result and client address, and send it back to the client using client_socket.send(response.encode()).

If the result is None, send an error message to the client using client_socket.send(b'Invalid expression\n').

If an exception occurs while handling the client, break out of the loop.
Print a message to indicate that the client has disconnected using print(f'Client disconnected: {client_address}'), and close the client socket using client_socket.close().

Define a main function.
Set the host IP address to '127.0.0.1', and the port number to 6969.

Set the maximum number of queued connections to 5.

Create a TCP/IP socket object using socket.socket(socket.AF_INET, socket.SOCK_STREAM).

Bind the socket to the host and port using server_socket.bind((host, port)).

Start listening for incoming connections using server_socket.listen(backlog).

Print a message to indicate that the server is running using print(f'Server started on {host}:{port}').

Create a thread-safe queue using connection_queue = queue.Queue(maxsize=backlog).

Create a while loop that continuously accepts incoming connections using server_socket.accept().

Print a message to indicate that a client has connected using print(f'Client connected from {client_address}').

Add the client socket and address to the connection queue using connection_queue.put((client_socket, client_address)).

If the connection queue is full, print a message indicating that the client is dropped, and close the client socket using client_socket.close().

While the connection queue is not empty, get the client socket and address from the queue using connection_queue.get().

Create a new thread to handle the client using client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address)).
Start the thread using client_thread.start().

Handle the KeyboardInterrupt exception by printing a message to indicate that the server has been stopped by the user, joining all threads except the main thread, closing all remaining client sockets, closing the server socket, and printing a message to indicate that the server socket has been closed.

----------------------------------------------------------------------------------------------------------
# testcases -->
all the test cases passed for the server2.py file. 
we evaluate it on 2 operands ,3 operands and even more it is working correctly. (with all operators like +,-,/,* in a expression.).We all test this code for multiple clients.



