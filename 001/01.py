import math
import timeit

###############PROBLEM 2###############
#Even Fibonacci numbers

def efibs(limit):
	n1 = 0
	n2 = 1
	temp = 0
	summ = 0
	fibs = []
	while n2 <= limit:
		fibs.append(n1)
		temp = n1 + n2
		n1 = n2
		n2 = temp
	fibs.append(n1)
	for x in fibs:
		if x%2 == 0:
			summ += x
	print(fibs)
	return summ

#######################################