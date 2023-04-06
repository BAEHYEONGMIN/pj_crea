#!python
import socket

# ip& port
ip = '218.52.71.205'
port = 9821

#클라이언트 소켓 준비
client = socket.socket()

#서버 접속
client.connect((ip,port))
print('connected')

#메시지 송신
client.send(bytes('hello','utf-8'))
print('-send-')

#메시지 입력
a = input(print('보낼 말?'))
client.send(bytes(a,'utf-8'))
print('-sended-')

#메시지 수신
msg = client.recv(1024).decode()
print('--msg recv--')
print(msg)

client.close()
