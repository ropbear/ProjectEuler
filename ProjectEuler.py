#PROJECT EULER
#This is practice to keep my python knowledge updated and refreshed.
import math



###############PROBLEM 1###############
#Multiples of 3 and 5

def multsTF(n):
	mults = []
	for num in range(n):
		if num%3 == 0 or num%5 == 0:
			mults.append(num)
	summ = 0
	for x in mults:
		summ += int(x)
	return summ

#######################################


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


###############PROBLEM 3###############
#Largest prime factor
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def list_divisors(n): #this can be improved upon, it's super slow dealing with ints that have 9 digits or more
	dlist = []
	for d in range(1,(n//2)+1):
		if n%d == 0:
			dlist.append(d)
	return dlist

def gen_primes(limit):
	plist = []
	for n in range(limit):
		if list_divisors(n) == [1]:
			plist.append(n)
	return plist

def LPF(n):
	l = len(str(n))
	digits = l//3
	plist = gen_primes(int(math.pow(10,digits)))
	plist.reverse()
	for num in plist:
		if n%num == 0:
			return num

#######################################


###############PROBLEM 4###############
#Largest Palindrome Product
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def FLP():
	pal = 0
	for num1 in range(999,99,-1):
		for num2 in range(999,99,-1):
			prod = num1*num2
			sprod = str(prod)
			l = len(sprod)
			m = l//2
			low = sprod[:m]
			high = sprod[m:]
			revhigh = ''
			for index in range(len(high)):
				revhigh += high[-(index+1)]
			if low == revhigh and prod > pal:
				pal = prod
	return pal


