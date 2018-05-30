def amicable(num):
	amicable_sum = 0
	for i in range(1,num):
		if num % i == 0:
			amicable_sum += i
	return amicable_sum

def sum_amicable_pairs(limit):
	ams = {}
	for num in range(1,limit):
		amsum = amicable(num)
		try:
			ams[amsum] = ams[amsum] + [num]
		except:
			ams[amsum] = [num]

	total = 0
	for value in ams.values():
		for num in value:
			if num in ams.keys():
				total += num + sum(ams[num])
	return total

if __name__ == "__main__":
	print(sum_amicable_pairs(10000))
