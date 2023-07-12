import socket
import pickle5 as pickle
a=10

myserver=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
myserver.bind((socket.gethostname(),5004))
myserver.listen(5)
while True:
    clt,adr=myserver.accept()
    print(f"connection to {adr} startes!")
    mylist={1:"server",2:"client"}
    mymsg=pickle.dumps(mylist)
    mymsg=bytes(f'{len(mymsg):<{a}}',"utf-8") + mymsg
    clt.send(mymsg)
    
    
    