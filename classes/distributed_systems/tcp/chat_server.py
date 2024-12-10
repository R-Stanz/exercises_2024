import socket			 
from datetime import datetime

s = socket.socket()		 
print ("Socket successfully created")

port = 12345			
s.bind(('', port))		 
print ("socket binded to %s" %(port)) 

s.listen(5)	 
print ("socket is listening")		 

while True: 

    c, addr = s.accept()	 
    print ('Got connection from', addr )
    
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c.send(f'{now}\tThank you for connecting.\nSend me a message: '.encode()) 

    try:
        message = c.recv(2048).decode()
        if message:
            print(f'<{addr}>\t{message}')
    except:
        pass

    c.close()

    break

