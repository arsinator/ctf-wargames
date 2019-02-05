import detectAesEcb
import base64

#KEY = bytes(detectAesEcb.generateRandomStr(16))
KEY = bytes("V"*16,"utf8") #static key for example
secretStr = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"

def equelBlocks(a):
	j = 0
	i = 0
	while i+32 < len(a):
		if a[i:i+16] == a[i+16:i+32]:
			j=j+1
		i = i+1
	if j!=0:
		j = j+1
	return j

def detectLen(blockSize):
	init = equelBlocks(detectAesEcb.oracle(bytes("A"*blockSize,"utf8")+base64.b64decode(secretStr),KEY))
	while(equelBlocks(detectAesEcb.oracle(bytes("A"*blockSize,"utf8")+base64.b64decode(secretStr),KEY)) == init):
		blockSize = blockSize - 1
	return blockSize

def ecbDecrypt(a): # a = 58
	result = ""
	init = detectAesEcb.oracle(bytes("A"*a,"utf8")+base64.b64decode(secretStr),KEY)[:a]
	for i in range(160):
		for j in range(0,127):
			if init == detectAesEcb.oracle(bytes("A"*(a-i)+result+chr(j),"utf8")+base64.b64decode(secretStr),KEY)[:a]:
				break
		result+=chr(j)
		init = detectAesEcb.oracle(bytes("A"*(a-i-1),"utf8")+base64.b64decode(secretStr),KEY)[:a]
	return result


print(ecbDecrypt(298))
print(detectLen(300))
