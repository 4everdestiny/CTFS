import libnum
from Crypto.Cipher import DES
from Crypto.Cipher import AES
def xor(s1,s2):
	print len(s1),len(s2)
	assert len(s1) == len(s2)
	res = ""
	for i in range(len(s1)):
		res += chr(ord(s1[i])^ord(s2[i]))
	return res

def sub(s,subvalue):
	res = ""
	for i in range(len(s)):
		res += chr((ord(s[i])-subvalue)%256)
	return res

def chrlen(s):
	print s
	res = ""
	for i in range(0,len(s),2):
		res += chr(int(s[i:i+2],16))
		print res
	return res
target = "4aee37c73d902a185407ebef96b2798539646536663335323135323035353636"
dec2 = libnum.n2s(int(target[32:],16))Common Crypto
#dec2 = target[32:]
target2 = libnum.n2s(int(target[:32],16))
data = "1B 2E 35 46 58 6E 72 86 9B A7 B5 C8 D9 EF FF 0C"
key = ""
for x in data.split(" "):
	key += x
key = libnum.n2s(int(key,16))
cipherX = AES.new(key, AES.MODE_ECB)
dec = cipherX.decrypt(target2)
print dec+dec2+"}"
#dec2 = cipherX.decrypt(xor(target[16:],target[:16]))