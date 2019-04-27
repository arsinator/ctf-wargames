import binascii
from math import ceil
from base64 import b64decode
from base64 import b64encode
from random import randint
from ctr import ctrEncr
import sys
sys.path.append("/Users/napster/Desktop/github/ctf-wargames/cryptopals/block crypto")
from CBCmodeAes import unPad, pk7, aesCbcEnc, aesCbcDec, aesEnc,xor


f = open("a.txt","r")
line = f.readline()
a = []
while line:
	a.append(ctrEncr(b64decode(line),"YELLOW SUBMARINE"))
	line = f.readline()
res = ""
tmp = bytearray(len(a))
print(a)
for i in range(9,10):
	l=0
	for j in a:
		tmp[l]= j[i]
		if i+16 < len(j):
			tmp += bytearray(chr(j[i+16]),"latin1")
		l += 1
		print(tmp)
	for j in range(0,256):
		x = bytearray(chr(j)*len(tmp),"latin1")
		x = xor(x,tmp)
	#	print(x)
		y = sum([not (31<i<127 or i == 13 or i == 10) for i in x])
		if y == 0 :
			print(x)
			res += chr(j)
		#	break
	tmp = tmp[:len(a)]

print(''.join([hex(ord(i))[2:] for i in res]))
