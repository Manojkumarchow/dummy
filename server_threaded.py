import socket as sc
from _thread import start_new_thread
serverSocket = sc.socket()
hostName = '127.0.0.1'
portNo = 8080
threads = 0
encodingType = 'utf-8'
try:
    serverSocket.bind((hostName, portNo))
except sc.error as error:
    print(str(error))
print('Waiting for a conn..')
serverSocket.listen(5)


def threaded_client(conn):
    conn.send(str.encode('Server is working:'))
    while True:
        data = conn.recv(2048)
        res = 'Server Says: ' + data.decode(encodingType)
        if not data:
            break
        conn.sendall(str.encode(res))
    conn.close()


while True:
    client, address = serverSocket.accept()
    address = address[0]
    port = address[1]
    print('Connected to: ' + address + ':' + str(port))
    start_new_thread(threaded_client, (client, ))
    threads += 1
    print('Thread Number: ' + str(threads))
serverSocket.close()
