import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define server address and port
server_address = ('127.0.0.1', 12345)

# Bind the socket to the server address and port
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print("Waiting for a connection...")

# Accept a connection
client_socket, client_address = server_socket.accept()
print("Connection established with:", client_address)

while True:
    # Receive data from the client
    data = client_socket.recv(1024).decode()
    
    if data == "exit":
        print("Connection closed by client.")
        break
    
    print("Received from client:", data)
    
    # Send a response back to the client
    response = "Server received: " + data
    client_socket.send(response.encode())

# Close the connection
client_socket.close()
server_socket.close()
