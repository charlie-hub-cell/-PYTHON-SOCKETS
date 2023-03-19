import socket
import operator
ip = '127.0.0.1'
port = 8080
SOCKET = (ip,port)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(SOCKET)
server.listen(1)
print("server started...")
print("waiting for client request..")
clientConnection,clientAddress = server.accept()
print("Connected client:", clientAddress)
msg = ''
while True:
    data,address = clientConnection.recvfrom(1024)
    msg = data.decode()
    if msg == "Over":
        print('connection is over')
        break
    print('Equation is received')
    result = 0
    operation_list = msg.split()
    oprnd1 = operation_list[0]
    operation = operation_list[1]
    oprnd2 = operation_list[2]
    num1 = int(oprnd1)
    num2 = int(oprnd2)
if operation == "+":
 result = num1+num2
elif operation == "-":
  result = num1-num2
elif operation == "/":
  result = num1/num2
elif operation == "*":
  result = num1*num2
print('send the result to the client')
output = str(result)
clientConnection.sendto(output.encode())
clientConnection.close()


