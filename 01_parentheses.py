#!/usr/bin/env python3

#Joshua Ching;The program will print argv with every other letter capitalized. 
#Then, will replace each capitalized vowel with a '*' and then tell you if '(' and ')' are balanced
#By Joching
#IMPORTANT: argv MUST start and end with -> "
#---------------------------------------------------

import sys

def main():
    rlist = ''
    e = 0
    arg = sys.argv[1]
    arg = str(arg)

    for i in arg:
        if i == '(':
            rlist = rlist + i
        elif i == ')':
            rlist = rlist + i
        elif i == ' ':
            rlist = rlist + i
        elif e == 1:
            rlist = rlist + i
            e = 0
        else:
            i = i.upper()
            rlist = rlist + i
            e = 1

    print(rlist)

    relist = rlist

    for x in relist:
        if x == 'O' or x == 'E' or x == 'A' or x == 'I' or x == 'U':
            relist = relist.replace(x,'*')

    print(relist)

    opencount = relist.count('(')
    closecount = relist.count(')')

    if opencount == closecount:
        print('Balanced? True')
    else:
        print('Balenced? False')

main()