import socket			 
from time import sleep
import concurrent.futures

def server_service():
    c, addr = s.accept()	 
    print ('Got connection from', addr )

    c.send('Thank you for connecting'.encode()) 
    c.close()


s = socket.socket()		 
print ("Socket successfully created")

port = 23456
s.bind(('', port))		 
print ("socket binded to %s" %(port)) 

s.listen(5)	 
print ("socket is listening")		 

connections_count = 0
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    while True: 
        future = executor.submit(server_service)
