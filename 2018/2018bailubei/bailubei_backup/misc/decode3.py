import os
index = 1000
index2 = 2320
res = ""
for i in range(index,index2+1,1):
    with open("win_mkj/{index}.txt".format(index=i),"rb") as f:
        res += f.read()
        f.close()
print res
a = []
for i in range(1000, 2321):
	a.append(os.fstat(os.open("win_mkj/{i}.txt".format(i=i), os.O_RDONLY)).st_atime) 
print a
for i in range(len(a)-1):
	print a[i+1] - a[i]
	if a[i+1] - a[i] < 0:
		raw_input()