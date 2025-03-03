import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1", 9999))

done = False

while not done:
	client_message = input("Client (You) : ")
	client.send(client_message.encode('utf-8'))
	if client_message == 'lav paka':
		done = True
	else:
		server_message = client.recv(1024).decode('utf-8')
		print(f"Server: {server_message}")
client.close()
