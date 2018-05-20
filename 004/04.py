import math
import timeit

###############PROBLEM 5###############
#Smallest Multiple
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def SmlMul(n):
	least = 0
	mul = 1
	for num in range(2,n+1):
		mul *= num
	low = n
	num = 1
	while num != mul:
		for num2 in range(n,0,-1):
			if num%num2 == 0:
				low = num2
				if low == 1:
					return num
			elif num%num2 != 0:
				break
		num += 1

#######################################