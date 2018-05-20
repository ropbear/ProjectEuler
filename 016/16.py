import math
import timeit

###############PROBLEM 17##############
#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

def num_to_alpha(): 
	##data##
	ot = {0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
	tens = {0:'',2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
	########

	##logic##
	sum = 0
	for num in range(1,1001): #inclusive
		#setup

		numl = list(str(num))
		l = len(numl)
		for num in range(0,l-1): numl[num] = int(numl[num])

		#parse
		word = ''
		if l == 1:
			word += ot[int(numl[0])]
		elif l == 2:
			if numl[l-2] == 1:
				word += ot[int(str(numl[l-2]) + str(numl[l-1]))]
			else:
				word += tens[int(numl[0])] + ot[int(numl[1])] 
		elif l == 3:
			word += ot[int(numl[0])]
			if int(numl[1]) == 0 and int(numl[2]) == 0:
				word += 'hundred'
			else:
				word += 'hundredand' 
			if numl[l-2] == 1:
				word += ot[int(str(numl[1]) + str(numl[2]))]
			else:
				word += tens[int(numl[1])] + ot[int(numl[2])]
		else:
			word += 'onethousand'
		print(word)
		sum += len(word)
	print(sum)
	#########

#######################################
