import math
import timeit

###############PROBLEM 13##############
#Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

def bigs():
	fil = open('problem13.txt','r')
	num = 0
	for line in fil:
		num += int(line)
	num = str(num)

	numlist = []
	for n in range(100):
		numlist.append(int(num[n*50:(n+1)*50]))

	return(str(sum(numlist))[:10])

#######################################
