import encryptMt
from random import randint

def crack(cypher):
	for seed in range(pow(2, 16)):
		possible_plaintext = encryptMt.encrypt_MT19937(cypher,seed)
		if possible_plaintext == bytearray("A" * 14,"latin1"):
			return seed

plaintext=bytearray("A" * 14,"latin1")
seed = randint(0, pow(2, 16))
print(seed)
ciphertext = encryptMt.encrypt_MT19937(plaintext, seed)
assert seed == crack(ciphertext)
