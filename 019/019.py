import math

def factorialSum(base):
	sumOfDigits = 0
	fact = str(math.factorial(base))
	for x in fact:
		sumOfDigits += int(x)
	return sumOfDigits

if __name__ == "__main__":
	print(factorialSum(100))

