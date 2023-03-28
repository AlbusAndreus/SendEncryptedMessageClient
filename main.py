import socket
from cryptography.fernet import Fernet
import time

def loadKey():
    file = open("C:\\Users\\Aleka\\OneDrive\\Desktop\\KeyFile.key")
    key = file.read()
    return key

message = input("Enter a message to encrypt and send")
key = loadKey()
f = Fernet(key)

encryptedMessage= f.encrypt(message.encode())
sock = socket.socket()
sock.connect(("localhost", 65000))

sock.send(encryptedMessage)
sock.close()
print("Message has gone through")


