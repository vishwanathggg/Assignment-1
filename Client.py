import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define server address and port
server_address = ('127.0.0.1', 12345)

# Connect to the server
client_socket.connect(server_address)

while True:
    # Get user input
    message = input("Enter a message to send to the server (type 'exit' to quit): ")
    
    # Send the message to the server
    client_socket.send(message.encode())
    
    if message == "exit":
        print("Connection closed.")
        break
    
    # Receive and display the response from the server
    response = client_socket.recv(1024).decode()
    print("Received from server:", response)

# Close the connection
client_socket.close()
