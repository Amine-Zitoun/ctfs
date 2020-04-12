import pickle
import numpy as np



data = pickle.load(open('model.pkl','rb'))
print (data.get_params())
import itertools
brute = False
if brute:
	for i in list(itertools.combinations(np.linspace(0,30),1)):
		print(i)
		print ('trying : '+str(i[0]))
		print (data.predict([[18,93,95,97,100]]))
else:
	f0 = 18
	f1 = 2
	f2 = 14
	f3 = 2
	f4 = 0
	pwd = "AA55aaaaaaaaaaaaaa"
	print(pwd)
	#pwd = "AAAAAaaaaaaaaaaaaa"
	print( [f0,f1,f2,f3,f4])
	print (data.predict([[f0,f1,f2,f3,f4]]))
	#flag = TG20{patterns_not_secured_by_AI}