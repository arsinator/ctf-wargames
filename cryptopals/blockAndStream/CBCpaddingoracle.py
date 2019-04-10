from base64 import b64decode
from base64 import b64encode
from random import randint
import sys
sys.path.append("/Users/napster/Desktop/crypto/ctf-wargames/cryptopals/block crypto")
from checkPadding import check
from CBCmodeAes import unPad, pk7, aesCbcEnc, aesCbcDec
from checkPadding import check
strings = ["MDAwMDAwTm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbmc=",
"MDAwMDAxV2l0aCB0aGUgYmFzcyBraWNrZWQgaW4gYW5kIHRoZSBWZWdhJ3MgYXJlIHB1bXBpbic=",
"MDAwMDAyUXVpY2sgdG8gdGhlIHBvaW50LCB0byB0aGUgcG9pbnQsIG5vIGZha2luZw==",
"MDAwMDAzQ29va2luZyBNQydzIGxpa2UgYSBwb3VuZCBvZiBiYWNvbg==",
"MDAwMDA0QnVybmluZyAnZW0sIGlmIHlvdSBhaW4ndCBxdWljayBhbmQgbmltYmxl",
"MDAwMDA1SSBnbyBjcmF6eSB3aGVuIEkgaGVhciBhIGN5bWJhbA==",
"MDAwMDA2QW5kIGEgaGlnaCBoYXQgd2l0aCBhIHNvdXBlZCB1cCB0ZW1wbw==",
"MDAwMDA3SSdtIG9uIGEgcm9sbCwgaXQncyB0aW1lIHRvIGdvIHNvbG8=",
"MDAwMDA4b2xsaW4nIGluIG15IGZpdmUgcG9pbnQgb2g=",
"MDAwMDA5aXRoIG15IHJhZy10b3AgZG93biBzbyBteSBoYWlyIGNhbiBibG93",
"QUJDREdGSkVQU0tGSkdISURPRURLR0pHTERKRXdkc2ZKSEZJRnIzMzI1Sm5jNDMz"]
randomAesKey="YELLOW SUBMARINE"
if "e" in sys.argv :
	rand = randint(0, 9)
	input = b64decode(strings[rand])
	print(input)
	a = pk7(input,16)
	print(a)
	b=aesCbcEnc(a,randomAesKey,bytes("\x00"*16,"latin1"))
	print(b)
	print(b64encode(b))

#decrypte last block 
if "d" in sys.argv :
	input = b64decode(sys.argv[2])
	inpb = bytearray(input)
	last = bytearray(inpb[-16:])
	first = bytearray(inpb[:-16])
	sol = ""
	beforeSol = ""
	tmp = bytearray()
	for i in range(1,16):
		for j in range(256):
			first1 = first[:-i]+(bytearray(chr(j),"latin1")+tmp)+last
			output = aesCbcDec(first1,randomAesKey, bytes("\x00"*16,"latin1"))
			if check(output,i):
				sol = chr(j^i^first[-i])+sol
				beforeSol = chr(ord(sol[0])^first[-i])+beforeSol
				tmp = bytearray()
				for k in range(len(sol)):
					tmp = tmp+bytearray(chr(ord(beforeSol[k])^(i+1)).encode("latin1")) 
				break
	print(sol)	
	output = aesCbcDec(input,randomAesKey, bytes("\x00"*16,"latin1"))
	print(output)

	
