import base64
import libnum
c1 = "AUikzgRpLWaVIEaeKrqkJiieLhhqvf4="
c2 = "AUikzgRpLWaVIEaeKrqkJiieLhhqvf6="
strings = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
head = "ISEC{"
head_base64 = "SVNFQ3s="
print strings[18],strings[21],strings[13],strings[15]
print bin(ord("I"))
info = "0" + bin(libnum.s2n(head))[2:]
print base64.b64encode(head)
m1 = base64.b64decode(c1)
print base64.b64encode(m1)
key = 3
print "A",strings.index("A"),bin(strings.index("A"))
print strings.index("S") - strings.index("A")
print "U",strings.index("U"),bin(strings.index("U"))
print strings.index("V") - 0b001010
print "i",strings.index("i"),bin(strings.index("i"))
print strings.index("N") - 0b010001
print "k",strings.index("k"),bin(strings.index("k"))
print strings.index("F") - 0b001001
print "z",strings.index("z"),bin(strings.index("z"))
print strings.index("Q") - 0b110011

def mybase64decode(strings,enc):
	res = ""
	for i in range(len(enc)):
		#print enc[i],strings
		res += bin(strings.index(enc[i]))[2:].rjust(6,"0")
	return libnum.n2s(int(res[:-1],2))

def mybase64decode2(strings,enc):
	res = ""
	for i in range(len(enc)):
		res += bin(strings.index(enc[i]))[2:].rjust(6,"0")
	return libnum.n2s(int(res[:-1],2))

def casear(m,key):
	res = ""
	for i in range(len(m)):
		res += chr((ord(m[i]) + key + i*2)%256)
	return res

def casear2(m,key):
	res = ""
	for i in range(len(m)):
		res += strings[(strings.index(m[i]) + key + i + 1)%len(strings)]
	return base64.b64decode(res)

print mybase64decode(strings,c1)
print base64.b64decode(c1)
print "0000000" + bin(libnum.s2n(base64.b64decode(c1)))[2:]
