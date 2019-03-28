import CBCmodeAes
import sys

key="YELLOW SUBMARINE"

def input(data):
	a= "comment1=cooking%20MCs;userdata="+data+";comment2=%20like%20a%20pound%20of%20bacon"
	a = CBCmodeAes.pk7(bytes(a,"utf8"),16)
	return CBCmodeAes.aesCbcEnc(a,key,bytes("\x00"*16,"utf8"))

def decode(data):
	b= CBCmodeAes.aesCbcDec(a,"YELLOW SUBMARINE",bytes("\x00"*16,"utf8"))
	b = CBCmodeAes.unPad(b)
	print(b)
	b = b.decode("latin1")
	return b.find(";admin=true;")

arg = sys.argv[1]
escaped = arg.translate(str.maketrans({";":  r"';'",
                                          "=":  r"'='"}))
print(escaped)
a = input(escaped)
print(a)
v="%20MCs;userdata="
f=" \x88|a\xd4\xb0\x0f\xa7\tp\xf0g\x83\x1f\xd7\x99"
gg=CBCmodeAes.xor(bytes(v,"latin1"),bytes(f,"latin1"))
print(CBCmodeAes.xor(gg,bytes(";admin=true;AAAA","latin1")))
a=bytearray(b'>\xdb(A\xfe\xad\t\xa6\x08`\xe78\xa3*\xf7\xe5\xfd\x1aTK\xdeG\xff\xffB1\x99\x12\x19s\xb9>\xf8pc?\x18\xd4B~\xa4Z\xf5\xc1CyR\x18\x8a|\xe1\xb4\xb8\xa6\xe6\xbd\xa3qm\xcdT.I\xf1\xbc\xf5\xbaZ\xb0t\xea\x97\tn\x8dq\xa8\xe0\xcbb\x9e\x99\x96\xa4\xfb\xbc{vEM\xbc\x1cJT;\xe8')
print(decode(a))
