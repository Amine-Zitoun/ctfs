import pickle

file = open('data','rb')
d = pickle.load(file)
flag = []
for i in d:
	if d[i] == "}":
		flag.append(d[i])
		break
	else:
		flag.append(d[i])
bginned = ['D', 'UCTF', '{']
nums_to_docode =[112, 49, 99, 107, 108, 51, 95, 121, 48, 117, 82, 95, 109, 51, 53, 53, 52, 103, 51]
end = ['}']
decoded = [chr(x) for x in nums_to_docode]

flag = ''.join(bginned+decoded+end)

print(flag)
'''new_flag = []
for i in d:
	if i.isalpha():
		new_flag.append(i)
	else:
		new_flag.append(chr(int(i)))
print(new_flag)'''
