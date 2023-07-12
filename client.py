import socket
myclient=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
myclient.connect((socket.gethostname(),5002))
msg=myclient.recv(1024)
print(msg.decode("utf-8"))