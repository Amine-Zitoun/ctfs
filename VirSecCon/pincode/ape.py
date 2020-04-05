from pwn import *



#I DELETED THE ACTUAL SCRIPT BY ACCIDENT SO YEAH SHIT
import itertools
import os

numbers = '0123456789'
y = ''
for c in itertools.product(numbers, repeat=4):
	s = remote('x.x.x.x',0)
	print s.recv()

    pin = y+''.join(c)
    print pin
    s.send(pin)
    print s.recv()