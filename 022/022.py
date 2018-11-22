#!/usr/bin/env python3

# Find the sum of all the positive integers which
# cannot be written as the sum of two abundant numbers.

LIMIT = 28124

def isAbundant(n):
    i = total = 0
    for i in range(1,n):
        total += i if n%i == 0 else 0
    return True if total > n else False

def main():
    # LOCAL VARIABLES
    abundants = []
    sums = set()
    unwriteables = []
    
    for i in range(1,LIMIT):
        if isAbundant(i):
            abundants.insert(0,i)
    print("[#] Abundants generated")

    for x in abundants:
        for y in abundants:
            sums.add(x+y)
    print("[#] Sums generated")

    for n in range(1,LIMIT):
        if n not in sums:
            unwriteables.insert(0,n)
    print("[#] Finished")

    retVal = sum(unwriteables)
    print(retVal)
    return retVal
    
if __name__ == "__main__":
    main()

