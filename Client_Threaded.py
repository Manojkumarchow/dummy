import socket as sc
client = sc.socket()
hostName = '127.0.0.1'
portNo = 8080
encodingType = 'utf-8'
print('Waiting for connection')
print('Welcome to the Server')
try:
    client.connect((hostName, portNo))
except sc.error as error:
    print(str(error))
res = client.recv(2048)
while True:
    message = input('Say Something: ')
    client.send(str.encode(message))
    res = client.recv(2048)
    print(res.decode(encodingType))
client.close()