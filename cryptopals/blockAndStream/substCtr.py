import binascii
from math import ceil
from base64 import b64decode
from base64 import b64encode
from random import randint
from ctr import ctrEncr
import sys
sys.path.append("/Users/napster/Desktop/github/ctf-wargames/cryptopals/block crypto")
from CBCmodeAes import unPad, pk7, aesCbcEnc, aesCbcDec, aesEnc,xor
def score(s):
    freq = {}
    freq[' '] = 700000000
    freq['e'] = 390395169
    freq['t'] = 282039486
    freq['a'] = 248362256
    freq['o'] = 235661502
    freq['i'] = 214822972
    freq['n'] = 214319386
    freq['s'] = 196844692
    freq['h'] = 193607737
    freq['r'] = 184990759
    freq['d'] = 134044565
    freq['l'] = 125951672
    freq['u'] = 88219598
    freq['c'] = 79962026
    freq['m'] = 79502870
    freq['f'] = 72967175
    freq['w'] = 69069021
    freq['g'] = 61549736
    freq['y'] = 59010696
    freq['p'] = 55746578
    freq['b'] = 47673928
    freq['v'] = 30476191
    freq['k'] = 22969448
    freq['x'] = 5574077
    freq['j'] = 4507165
    freq['q'] = 3649838
    freq['z'] = 2456495
    score = 0
    for c in s.lower():
        if c in freq:
            score += freq[c]
    return score

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
	prev = 0
	for j in range(0,256):
		x = bytearray(chr(j)*len(tmp),"latin1")
		x = xor(x,tmp).decode("latin1")
	#	print(x)
		y = score(x)
		if y > prev :
			prev = y
			print(x)
		"""y = sum([not (31<i<127 or i == 13 or i == 10) for i in x])
		if y == 0 :
			print(x)
			res += chr(j)
		#	break
		"""
	tmp = tmp[:len(a)]

print(''.join([hex(ord(i))[2:] for i in res]))
