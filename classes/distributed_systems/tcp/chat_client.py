# Import socket module 
import socket			 

# Create a socket object 
s = socket.socket()		 

# Define the port on which you want to connect 
port = 12345			

# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 

# receive data from the server and decoding to get the string.
server_msg = s.recv(2048).decode()
reply_msg = input(server_msg)
s.send(reply_msg.encode())
# close the connection 
s.close()	 
	

