import socket
ip = '127.0.0.1'
port = 8080
SOCKET = (ip,port)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(SOCKET)
while True:
    print("example: 4+5")
    inp = input("Enter the operation in \ the form operand operator operand:")
    if inp == "Over":
        break
    print('message being sent to server: ' + inp + '\n')
    client.send(inp.encode())
    answer = client.recv(2048)
    print("answer is" + answer.decode())
    print("Type 'Over' to terminate")
    client.close()