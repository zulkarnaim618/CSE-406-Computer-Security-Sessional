import socket
import math
import random
aes = __import__("1905016_aes")
elliptic = __import__("1905016_elliptic")


s = socket.socket()
port = 55555

s.bind(('', port))

s.listen(5)

client, addr = s.accept()
print ('Got connection from', addr )


a = int(client.recv(1024).decode())
client.send("ack".encode())
b = int(client.recv(1024).decode())
client.send("ack".encode())
p = int(client.recv(1024).decode())
client.send("ack".encode())
gx = int(client.recv(1024).decode())
client.send("ack".encode())
gy = int(client.recv(1024).decode())
client.send("ack".encode())
kagx = int(client.recv(1024).decode())
client.send("ack".encode())
kagy = int(client.recv(1024).decode())
client.send("ack".encode())

# print(a)
# print(b)
# print(p)
# print(gx)
# print(gy)
# print(kagx)
# print(kagy)

kb = random.randrange(2,int(p+1-2*math.sqrt(p)))
(kbgx,kbgy) = elliptic.pointAddDouble((gx,gy),a,kb,p)


client.send(str(kbgx).encode())
client.recv(1024).decode()
client.send(str(kbgy).encode())
client.recv(1024).decode()

(kabgx,kabgy) = elliptic.pointAddDouble((kagx,kagy),a,kb,p)

# print(kabgx)
# print(kabgy)

length = 128
keyData = elliptic.makeData(kabgx,length)
keys = aes.generateKeys(keyData)



while True:
    cypherMsg = client.recv(1024).decode()
    ivString = cypherMsg[:aes.length]
    iv = []
    for i in ivString:
        iv.append(ord(i))
    msgStringWhole = cypherMsg[aes.length:]
    msgData = []
    for i in range(0, len(msgStringWhole), aes.length):
        temp = []
        for j in msgStringWhole[i:i + aes.length]:
            temp.append(ord(j))
        msgData.append(temp)

    decryptedMsgData = aes.decrypt(iv, keys, msgData)

    print("Msg received: ", end='')
    msgString = ""
    for i in decryptedMsgData:
        for j in i:
            print(chr(j), end='')
            msgString += chr(j)
    print()
    if (msgString.rstrip()=="q"):
        break

client.close()
s.close()



