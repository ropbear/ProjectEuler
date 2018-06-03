def sum_divisors(num):
	divisor_sum = 0
	for i in range(1,num):
		if num % i == 0:
			divisor_sum += i
	return divisor_sum

def sum_amicable_pairs(limit):
	#pairs = [[0]*limit]*limit #create a (limit,limit) matrix for memoization
	#This actually just makes 'limit' rows of the same object... so any change happens to them all
	#here is the proper way...
	pairs = [[0 for x in range(limit)] for y in range(limit)]
	for num in range(1,limit):
		dsum = sum_divisors(num)
		try:
			pairs[num][dsum] = 1
		except:
			pass #ignore sums of the proper divisors that are over the limit

	total = 0 
	#[print(x) for x in pairs] < Easy way to print a matrix
	for x in range(limit):
		for y in range(limit):
			if x != y and pairs[x][y] == 1 and pairs[y][x] == 1:
				print(x,y)
				pairs[y][x] = 0
				total += (x + y)
			
	return total

if __name__ == "__main__":
	print(sum_amicable_pairs(10000))
