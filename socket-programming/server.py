import socket
myserver=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
myserver.bind((socket.gethostname(),5002))
myserver.listen(5) 
while True:
 clt,adrs=myserver.accept()
 print(f"client address is {adrs} connected")
 clt.send(bytes("first socket programming","utf-8"))
 clt.close()