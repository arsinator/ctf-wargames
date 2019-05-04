from mt19937 import MT19937

from random import randint
from time import sleep,time
def getNumber():
	#sleep(randint(40, 1000))
	seed = int(time())
	print("Seed : %d" %seed)
	rand_int = MT19937(seed).random()
	#sleep(randint(44, 1000))
	return rand_int

def crack_seed():
	rand_int = getNumber()
	current_time = int(time())
	for seed in range(current_time, current_time - 2500, -1):
		if MT19937(seed).random() == rand_int:
			return seed
	raise Exception('Could not crack MT19937 seed.')

print(crack_seed())
