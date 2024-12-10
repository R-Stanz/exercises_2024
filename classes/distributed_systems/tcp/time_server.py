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
    c.send(f'{now}\tThank you for connecting.'.encode()) 

    c.close()

    break

