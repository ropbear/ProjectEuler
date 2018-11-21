#!/usr/bin/env python3

# GLOBALS
alphabet = [
        '','a','b','c','d','e','f','g','h',
        'i','j','k','l','m','n','o','p','q',
        'r','s','t','u','v','w','x','y','z'
    ]

# FUCTIONS
def alphabetValue(string):
    sum = 0
    for ch in string:
        try:
            sum += alphabet.index(ch.lower())
        except:
            print("[!] bad char: "+ch)
            pass
    return sum

def main():
    try:
        f = open("names.txt",'r')
    except FileNotFoundError:
        print("[!] Error: failed to read file")
        return 0

    lines = [x for x in f]
    names = [name[1:-1] for name in lines[0].split(',')]
    names.sort()
    total = 0
    for index in range(0,len(names)):
        total += ((index+1) * alphabetValue(names[index]))
    print("[#] Total: "+str(total))
    return total

if __name__ == "__main__":
    main()
