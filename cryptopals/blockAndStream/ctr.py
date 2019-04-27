from base64 import b64decode
from base64 import b64encode
from random import randint
import sys
sys.path.append("/Users/napster/Desktop/github/ctf-wargames/cryptopals/block crypto")
from CBCmodeAes import unPad, pk7, aesCbcEnc, aesCbcDec, aesEnc,xor

cr = b64decode("L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==")
print(len(cr))
u=aesEnc("\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00","YELLOW SUBMARINE")+aesEnc("\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00","YELLOW SUBMARINE")+aesEnc("\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00","YELLOW SUBMARINE")

print(xor(cr,u))


