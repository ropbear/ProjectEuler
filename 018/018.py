#!/usr/env/python3

'''
1 Jan 1900 was a Monday
30 days for Sept, Apr, June, Nov
28 for Feb (29 on leap years)
	A leap year occurs on any year evenly divisible by 4...
		but not on a century unless it is divisible by 400.
31 days for every other month.

I do not intend for this to be efficient, it's more fun this way than using mathematics
to reduce the line count.
'''
def days(date):
	#date:[day, month, year]
	#includes the end date
	thirties = [4,6,9,11]
	working_date = [1,1,1901] # [1, Jan, 1900]
	count = 0
	while working_date != date:
		leap = False
		if working_date[2]%4 == 0:
			if working_date[2]%1000 == 0:
				leap = (working_date[2]%400 == 0)
			else:
				leap = True

		if working_date[1] == 12 and working_date[0] == 31:
			working_date = [1,1,working_date[2]+1]
			
		elif working_date[1] == 2 and working_date[0] >= 28:
			if leap:
				#iterate one more day before iterating month
				if working_date[0] == 29:
					working_date[0] = 1
					working_date[1] += 1
				else:
					working_date[0] += 1
			else:
				working_date[0] = 1
				working_date[1] += 1

		else:
			if working_date[0] == 30 and working_date[1] in thirties:
				working_date[0] = 1
				working_date[1] += 1
			elif working_date[0] == 31 and working_date[1] not in thirties:
				working_date[0] = 1
				working_date[1] += 1
			else:
				working_date[0] += 1

		count += 1
	return count

if __name__ == '__main__':
	i = days([31,12,2000])
	print(i//7)

