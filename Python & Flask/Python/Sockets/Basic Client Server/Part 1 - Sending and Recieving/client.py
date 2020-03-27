import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) # intialize the socket object with IPv4 and use TCP packets
s.connect((socket.gethostname(),1234)) #connect to the server address

'''
msg=s.recv(1024) #get the bytes
print(msg.decode("utf-8"))# decode the bytes into proper format
'''


full_msg = ''
while true:
     msg = s.recv(8)
     if len(msg)<=0:
         break
     full_msg+=msg.decode("utf-8")

 print(full_msg)