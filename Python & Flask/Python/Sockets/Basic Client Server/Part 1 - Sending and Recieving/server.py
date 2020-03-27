import socket

HEADERSIZE = 10

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) # intialize the socket object with IPv4 and use TCP packets
s.bind((socket.gethostname(),1234)) #bind the server ip address with a port
print(f"[*] Server started and listening")
s.listen(5) #Only 5 Connection at a time


while True:
    clientSocket, clientAddress = s.accept()# Accept connection, and get client's ip and their port no.
    print(f"[*] Connection Established with {clientAddress}")
    
    msg = "Welcome to the Server!"
    msg = f'{len(msg):<{HEADERSIZE}}'+msg
    
    clientSocket.send(bytes({msg},"utf-8"))# also send a connection confirmation to client
    clientSocket.close() # close the connection

