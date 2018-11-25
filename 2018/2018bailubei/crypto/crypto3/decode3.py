import libnum
n = 829467319
e = 48357
print libnum.factorize(n)
p = 36497
q = 22727
phi = (p-1)*(q-1)
d = libnum.invmod(e,phi)
res = ""
with open("Crypt_three.txt","r") as f:
	info = f.readline()
	while info:
		info = f.readline()
		if info == "":
			break
		res += libnum.n2s(pow(int(info),d,n))
print res
res += ""
print len(res)
res2 = ""
print res[::-1]
index = 0
temp = index
res2 = ""
for i in range(len(res)):
	res2 += res[::-1][temp]
	temp = (temp+5)%len(res)
print res2
