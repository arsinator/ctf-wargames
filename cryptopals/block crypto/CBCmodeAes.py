import base64
from Crypto.Cipher import AES

def pk7(a,b):
    c = len(a)%b
    d = b - c
    return a + bytearray(chr(d)*d,"utf8")

def xor(a,b):
    c = bytearray(len(a))
    for i in range(0,len(a)):
        c[i] = a[i] ^ b[i]
    return c

def aesEnc(text,key):
    obj = AES.new(key, AES.MODE_ECB)
    # return bytearray(obj.encrypt(bytes(text,"utf8")))
    return bytearray(obj.encrypt(text))

def aesDec(text,key):
    obj = AES.new(key, AES.MODE_ECB)
    return bytearray(obj.decrypt(text))

def aesCbcEnc(text,key,iv):
    result = bytearray(len(text))
    for i in range(0,len(text),16):
        result[i:i+16] = aesEnc(bytes(xor(text[i:i+16],iv)),key)
        iv = result[i:i+16]
    return result

def aesCbcDec(text,key,iv):
    result = bytearray(len(text))
    for i in range(0,len(text),16):
        result[i:i+16] = xor(aesDec(bytes(text[i:16+i]),key),iv)
        iv = text[i:16+i]
    return result

a = aesCbcEnc(bytes("abcdabcd12345678","utf8"),"YELLOW SUBMARINE",bytes("\x00"*16,"utf8"))
print(base64.b16encode(bytes(a)))
b = aesCbcDec(a,"YELLOW SUBMARINE",bytes("\x00"*16,"utf8"))
print(b)
f = open("file.txt","r")
allLine = ""
for line in f:
    allLine+=line

decodedLine = base64.b64decode(bytes(allLine,"utf8"))
decodedLine = pk7(decodedLine,16)

print(aesCbcDec(decodedLine, "YELLOW SUBMARINE",bytes("\x00"*16,"utf8")))
