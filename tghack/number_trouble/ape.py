str_a = '84 71 50 48 123 110 117 109 98 101 114 115 95 97 110 100 95 116 101 120 116 95 103 111 101 115 95 104 97 110 100 95 105 110 95 104 97 110 100 125'
new_a  = ''
#print chr(71)
#print str_a.split(' ')
for i in str_a.split(' '):
	#print( chr(int(i)))
	#print (int(i))
	new_a += str(chr(int(i)))
print( new_a)