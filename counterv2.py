# РАндомные числа в заданых пределах и заданом количестве
lst = []
dct = {}
def make_list (minimum, maximum, qty):
	from random import random
	for i in range(qty):
		lst.append (int (random() * (maximum - minimum + 1)) + minimum)

def analysis():
	for i in lst:
		if i in dct:
			dct[i] +=1
		else:
			dct[i] = 1

mn = int (input ("Minimum: "))
mx = int (input ("Maximum: "))
qty = int (input ("Number of elements: "))
make_list (mn, mx, qty)
analysis ()
for i in sorted(dct):
	print ("'%d': %d" % (i, dct[i]))

input()