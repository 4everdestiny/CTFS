import libnum
from Crypto.Cipher import DES
from Crypto.Cipher import AES
target = "4aee37c73d902a185407ebef96b2798539646536663335323135323035353636"
dec2 = libnum.n2s(int(target[32:],16))
#dec2 = target[32:]
target2 = libnum.n2s(int(target[:32],16))
data = "1B 2E 35 46 58 6E 72 86 9B A7 B5 C8 D9 EF FF 0C"
key = ""
for x in data.split(" "):
	key += x
print key,len(key)
key = libnum.n2s(int(key,16))
print key,len(key)
IV = "\x00"*16
cipherX = AES.new(key, AES.MODE_ECB)
dec = cipherX.decrypt(target2)
print dec,len(dec)
print dec+dec2+"}"
#dec2 = cipherX.decrypt(xor(target[16:],target[:16]))