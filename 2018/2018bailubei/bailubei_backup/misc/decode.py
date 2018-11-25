def sub(a,key):
    return int(bin(a)[2:][-key:] + bin(a)[2:][:-key],2)

def calcu1(a):
    return 15 * (a >> 16) + (a & 65535)

def calcu2(a,b):
    return ((b % 65521) << 16) | (a % 65521)

def adler32(string):
    a = 1
    b = 0
    for i in range(len(string)):
        a += ord(string[i])
        b += a
    a = calcu1(a)
    b = calcu1(b)
    return calcu2(a,b)

target = adler32("0x1011")
print hex(target)
print hex(adler32("1v2011"))
res = ""
for i in range(0x20,128):
    res += chr(i)
print res
test = 0xfffff