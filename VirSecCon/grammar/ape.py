from pwn import *
flag = "LLS{"


# Same thing that happened to pin code deleted it by accident because i'm stupid
s = remote('x.x.x.x',0)

def check():
	if s.recv().split('\n')[-3].split(' ')[-1][:-1] == "CORRECT":
		return "TRUE"
	else:
		return "FALSE"



def bruteforce(s):
	if s[-1] == "}":
		print "WE DONE IT BOYS"
		print s
	else:
		for i in string.printable:
			s.send(s+i)
			if check() == "TRUE":
				flag = flag + i
				bruteforce(flag)
			else:
				pass

bruteforce(flag)