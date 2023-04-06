from socket import *
import threading
import time
import sys

def send(socket):
        while True:
            send_Data = input('>>')
            socket.sendall(send_Data.encode('utf-8'))
            if send_Data == 'exit':
                break
        clientSocket.close()
def receive(socket):
        while True:
            recv_Data = socket.recv(1024)
            print('상대방 : ', recv_Data.decode('utf-8'))

port = 31415
ip = '218.52.71.205'
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((ip, port))

print('접속 완료')

sender = threading.Thread(target = send, args=(clientSocket,))
receiver = threading.Thread(target = receive, args=(clientSocket,))

sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass
