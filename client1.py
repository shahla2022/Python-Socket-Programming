import pickle5 as pickle
import socket
a=10
myclient=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
myclient.connect((socket.gethostname(),5004))
while True:
    complete_info=b''
    rec_msg=True
    while True:
        mymsg=myclient.recv(16)
        if rec_msg:
            print(f"The length of my message is = {mymsg[:a]}")
            x=int(mymsg[:a])
            rec_msg=False
        complete_info +=mymsg
        if len(complete_info)-a == x:
            print("Recieved data is:")
            print(complete_info[a:])
            m=pickle.loads(complete_info[a:])
            print(m)
            rec_msg=True
            complete_info=b''
        print(complete_info)

     

