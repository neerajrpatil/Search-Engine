""""
CN Group Project Work

Group Members:
Nishan Holla PES2UG21CS340
Neeraj Patil PES2UG21CS328
Nishank Koul PES2UG21CS342

"""

import socket
import threading

print('[starting] server is starting... \n \nWelcome to CHAT NNN !\n ')

host = socket.gethostbyname(socket.gethostname())
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

client, address = server.accept()
print("Connected with {}".format(str(address)))

client.send('Connected to server!'.encode('ascii'))

quest = ["best college","best subject","fruit","food","vegetable","pizza","sandwich","hello","creator","transport layer protocols","application layer protocol","network layer protocol","team name","best shampoo","best teacher","best milk","best ice cream","best dosa","best biriyani","tcp","udp","burger","best political party","best leader"]
answ = ["PESU ECC ","Computer Networks","Apple","Chole bature","carrot","dominos","cool joint","nice to meet you","Nishan Neeraj Nishank","TCP UDP" ,"HTTP FTP SMTP " , "IP","NNN ","SUNSILK","DR ANNAPURNA","NANDINI","Corner House","MTR","Meghana's","transport layer protocol","user datagram protocol","mcdonald's","BJP","Narendra Modi"]

def broadcast(message):
    ans = '{}'.format(message)
    client.send(ans.encode('ascii')) 

def handle(client):
    while True:
        message = client.recv(1024).decode('ascii')
        ref = "Query : "+message
        client.send(ref.encode('ascii'))
        i=0
        while i<len(quest):
            if message == quest[i]:
                broadcast(answ[i])
                break
            i=i+1

        if i==len(quest):
            broadcast("Sorry I dont have the answer to "+message)

thread = threading.Thread(target=handle, args=(client,))
thread.start()


 


