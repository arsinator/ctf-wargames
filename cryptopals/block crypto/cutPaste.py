from urllib.parse import parse_qs
import CBCmodeAes

key="YELLOW SUBMARINE"
def create(email):
	url = "email="+email+"&uid=2&role=user"
	a = CBCmodeAes.pk7(bytes(url,"utf8"),16)
	return CBCmodeAes.aesEnc(a,key)

def register(a):
	text = CBCmodeAes.aesDec(a,key)
	return  parse_qs(CBCmodeAes.unPad(text),strict_parsing=True)

a=create("B"*10+"B"*4)[:-16]+create("B"*10+"admin"+"\x0b"*11)[16:32]
print(register(bytes(a)))
