#!/usr/bin/env python3

#Joshua Ching ; This code will take your per ------finish later---------
# (running your code?)
#By Joching

import sys


def start_function():

    if sys.argv[1] == 'RAINBOW':
        print('hi')
    else:
        a = input('What do you want to print? ')
        b = input('What color do you want? ')
        c = input('What kind of font/formatting do you want? ')
        d = input('What kind of background do you want? ')
        b = int(b)
        c = int(c)
        d = int(d)

        def white_colorful_text(a,b,c,d):
            print('\033[{1};{2};{3}m {0} \033[0m'.format(a,b,c,d))
        white_colorful_text(a,b,c,d)




start_function()











