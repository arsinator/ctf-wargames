def check(a):
	b = a[len(a)-ord(a[-1]):]
	print(b)
	if b == len(b) * b[0]:
		return True
	else:
		raise ValueError('wrong Padding')

if __name__ == '__main__':
	check("\x41\x41\x41\x41")

