

import base64
import os
with open('msg.txt',r) as f:
	msg = f.read()


def decode(s):

	try:
		decode(base64.b64decode(s))
	except Exception as e:
		print "Found it "
		print s



decode(msg)