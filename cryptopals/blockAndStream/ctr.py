from math import ceil
from base64 import b64decode
from base64 import b64encode
from random import randint
import sys
sys.path.append("/Users/napster/Desktop/github/ctf-wargames/cryptopals/block crypto")
from CBCmodeAes import unPad, pk7, aesCbcEnc, aesCbcDec, aesEnc,xor

cr = b64decode("L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==")
print(len(cr))
u=aesEnc("\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00","YELLOW SUBMARINE")+aesEnc("\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00","YELLOW SUBMARINE")+aesEnc("\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00","YELLOW SUBMARINE")
def ctrEncr(txt,key):
	nonce = bytearray("\x00"*16,"latin1")
	res = bytearray()
	for i in range(0,ceil(len(txt)/16)):
		nonce[8]=i
		res += aesEnc(nonce.decode("latin1"),key)
	return xor(res,txt)
print(xor(cr,u))

print(ctrEncr(cr,"YELLOW SUBMARINE"))
