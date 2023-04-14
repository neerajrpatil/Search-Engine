""""
CN Project

Group Members:
Nishan Holla PES2UG21CS340
Neeraj Patil PES2UG21CS328
Nishank Koul PES2UG21CS342

"""

import socket
import threading

host = socket.gethostbyname(socket.gethostname())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, 55555))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            print(message)
        except:
            print("An error occured!")
            client.close()
            break

def write():
    while True:
        query = '{}'.format(input(''))
        client.send(query.encode('ascii'))

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
