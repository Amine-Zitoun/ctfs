# uncompyle6 version 3.6.5
# Python bytecode 3.7 (3394)
# Decompiled from: Python 2.7.17 (default, Nov  7 2019, 10:07:09) 
# [GCC 7.4.0]
# Warning: this version has problems handling the Python 3 byte type in contants properly.

# Embedded file name: keygame.py
# Size of source mod 2**32: 1496 bytes
import base64
from itertools import cycle

class myGame:

    def __init__(self, xdim=4, ydim=4):
        self.x = xdim
        self.y = ydim
        self.matrix = []
        for i in range(self.x):
            row = []
            for j in range(self.y):
                row.append(0)

            self.matrix.append(row)

    def make_keys(self, *args, **kwargs):
        words = []
        with open('wordlist.txt') as (f):
            for line in f:
                words.append(line.strip())
            print (len(words))
            for i in range(self.x):
                for j in range(self.y):
                    self.matrix[j][i] = words[(i + j)]
        #print (self.matrix[self.y-1][self.x-1])

        keyArray = []
        keyArray.append(self.matrix[args[0]][args[1]])
        keyArray.append(self.matrix[args[2]][args[3]])
        #print (keyArray)
        key = ''
        for k in keyArray:
            key = key.strip() + str(k).strip()

        #print(key)
        return key

    def checkdata(self, key):
        f = base64.b64decode('NSYDUhoVWQ8SQVcOAAYRFQkORA4FQVMDQQ5fQhUEWUYMDl4MHA==')
        data = f.decode('utf-8')
        #print( data)
        c = ''.join((chr(ord(c) ^ ord(k)) for c, k in zip(data, cycle(key))))
        if c[11] == "l":
            print ("YO BOY STOP")
        print('%s' % (c))


if __name__ == '__main__':
    mgame = myGame(25, 25)
    brute=  False
    if (brute):

        for x in range(15,25):
            for y in range(15,25):
                for x1 in range(25):
                    for y1 in range(25):
                        print ("=======================")
                        print ("X: "+str(x))
                        print ("Y: "+str(y))
                        print ("X1: "+str(x1))
                        print ("Y1:" +str(y1))
                        print ("======================")
        #x = input('input a number: ')
        #y = input('input a number: ')
        #x1 = input('input a number: ')
        #y1 = input('input a number: ')
                        data = mgame.make_keys(x, y, x1, y1)
                        mgame.checkdata(data)
    else:
        #x= 15
        y=12
        y1= 23
        x1 = 8
        for x in range(25):
            print ("TESTING: "+str(x))
            data = mgame.make_keys(x, y, x1, y1)
            mgame.checkdata(data)