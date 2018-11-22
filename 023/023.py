import math

def lexPerm(chars,nth):
    index = nth-1
    if len(chars) == 1:
        return chars[0]
    else:
        size = math.factorial(len(chars)-1)
        ch = chars[index//size]
        chars.remove(ch)
        return ch+lexPerm(chars,nth%size)

if __name__ == "__main__":
    # specific for project euler
    print(lexPerm([str(digit) for digit in range(0,10)],1000000))

