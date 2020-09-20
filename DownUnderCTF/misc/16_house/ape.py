import base64

with open('ci.txt','rb') as f:
	r = f.readline()
#print(r.split(b'\n')[0])
print(base64.b64decode(r.split(b'\n')[0].decode('utf-8')+"==").decode('utf-8'))