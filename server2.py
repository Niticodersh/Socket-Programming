import socket  # import the socket module for networking
import threading  # import the threading module for concurrent execution
import re  # import the regular expressions module for string pattern matching
import queue  # import the queue module for thread-safe communication

def handle_client(client_socket, client_address):
    while True:
        try:
            data = client_socket.recv(1024)  # receive data from the client
            if not data:  # if no data is received, break out of the loop
                break
            expression = data.decode().strip()  # decode the data and remove any whitespace
            result=eval(expression)  # evaluate the expression
            if result is not None:  # if a result is obtained from the evaluation
                    response = f'{result} (client: {client_address})\n'  # create a response with the result and client address
                    client_socket.send(response.encode())  # send the response to the client
            else:
                client_socket.send(b'Invalid expression\n')  # if the expression is invalid, send an error message to the client
        except:  # if an exception occurs while handling the client, break out of the loop
            break

    print(f'Client disconnected: {client_address}')  # print a message when the client disconnects
    client_socket.close()  # close the client socket

def main():
    host = '127.0.0.1'  # set the server's IP address to localhost
    port = 6969  # set the server's port number
    backlog = 5  # set the maximum number of queued connections
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create a TCP/IP socket object
    server_socket.bind((host, port))  # bind the socket to the host and port
    server_socket.listen(backlog)  # start listening for incoming connections
    print(f'Server started on {host}:{port}')  # print a message to indicate that the server is running
    connection_queue = queue.Queue(maxsize=backlog)  # create a thread-safe queue to hold incoming connections
    try:
        while True:
            try:
                client_socket, client_address = server_socket.accept()  # accept incoming connections
                print(f'Client connected from {client_address}')  # print a message when a client connects
                connection_queue.put((client_socket, client_address))  # add the client socket and address to the connection queue
            except queue.Full:  # if the connection queue is full, drop the client
                print(f'Connection queue is full, dropping client {client_address}')
                client_socket.close()  # close the client socket
            while not connection_queue.empty():  # process incoming connections in the queue
                client_socket, client_address = connection_queue.get()  # get the client socket and address from the queue
                client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))  # create a new thread to handle the client
                client_thread.start()  # start the thread
    except KeyboardInterrupt:  # if the server is interrupted by the user
        print('Server stopped by keyboard interrupt')
        for thread in threading.enumerate():  # join all threads except the main thread
            if thread != threading.current_thread():
                thread.join()
        for client_socket, client_address in list(connection_queue.queue):  # close all remaining client sockets
            client_socket.close()
            print(f'Client disconnected: {client_address}')
        server_socket.close()  # close the server socket
        print('Server socket closed')
if __name__ == '__main__':
    main()
