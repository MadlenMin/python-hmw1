import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 9999))

server.listen()

print("I am listening")

client , addr = server.accept()

done = False

while not done:
	message = (client.recv(1024).decode('utf-8'))
	if message == 'lav paka':
		done = True
	else:
		print(f" Client : {message}")
		server_message = input("Server: ")
		client.send(server_message.encode('utf-8'))
client.close()
server.close()


