import socket
import math
import random
import sympy
aes = __import__("1905016_aes")
elliptic = __import__("1905016_elliptic")

s = socket.socket()
port = 55555

s.connect(('127.0.0.1', port))

# a = 2
# b = 2
# p = 17
# gx = 5
# gy = 1
# ka = 3

length = 128
p = sympy.randprime(pow(2, length - 1), pow(2, length))
(a,b) = elliptic.generateRandomCurve(p)
(gx,gy) = elliptic.generateRandomPoint(a,b,p)
ka = random.randrange(2,int(p+1-2*math.sqrt(p)))
(kagx,kagy) = elliptic.pointAddDouble((gx,gy),a,ka,p)



s.send(str(a).encode())
s.recv(1024).decode()
s.send(str(b).encode())
s.recv(1024).decode()
s.send(str(p).encode())
s.recv(1024).decode()
s.send(str(gx).encode())
s.recv(1024).decode()
s.send(str(gy).encode())
s.recv(1024).decode()
s.send(str(kagx).encode())
s.recv(1024).decode()
s.send(str(kagy).encode())
s.recv(1024).decode()


kbgx = int(s.recv(1024).decode())
s.send("ack".encode())
kbgy = int(s.recv(1024).decode())
s.send("ack".encode())

# print(kbgx)
# print(kbgy)

(kabgx,kabgy) = elliptic.pointAddDouble((kbgx,kbgy),a,ka,p)

# print(kabgx)
# print(kabgy)



keyData = elliptic.makeData(kabgx,length)
keys = aes.generateKeys(keyData)

while True:
    msgString = input("Enter msg to send or q to quit: ")
    msgStringWhole = msgString
    if len(msgStringWhole)%aes.length!=0:
        for i in range(0,aes.length-len(msgStringWhole)%aes.length):
            msgStringWhole += " "
    msgData = []
    for i in range(0,len(msgStringWhole),aes.length):
        temp = []
        for j in msgStringWhole[i:i+aes.length]:
            temp.append(ord(j))
        msgData.append(temp)

    (iv, encryptedMsgData) = aes.encrypt(msgData,keys)

    cypherMsg = ""
    for i in iv:
        cypherMsg += chr(i)
    for i in encryptedMsgData:
        for j in i:
            cypherMsg += chr(j)
    s.send(cypherMsg.encode())
    if msgString=="q":
        break
s.close()


