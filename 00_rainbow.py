#!/usr/bin/env python3

#Joshua Ching ; Prints colored text. 
#Follow the promts. Type "Rainbow" to have the word rainbow printed in rainbow colors
#By Joching
#------------------------------------------------------------

import sys

def main():
    a = input('What do you want to print? ')
    if a.lower() == 'rainbow':
        sys.stdout.write('\033[31mR\033[0m')
        sys.stdout.write('\033[32mA\033[0m')
        sys.stdout.write('\033[33mI\033[0m')
        sys.stdout.write('\033[34mN\033[0m')
        sys.stdout.write('\033[35mB\033[0m')
        sys.stdout.write('\033[31mO\033[0m')
        sys.stdout.write('\033[32mW\033[0m')

        print('')
    else:
        b = input('What color do you want the text to be?\nBlack = 30\nRed = 31\nGreen = 32\nYellow = 33\nBlue = 34\nPurple = 35\nCyan = 36\nWhite = 37\n')
        c = input('What kind of font/formatting do you want?\n(No color) = 0\n(Color) = 1\nUnderline = 4\n')
        d = input('What color do you want the background to be?\nBlack = 40\nRed = 41\nGreen = 42\nYellow = 43\nBlue = 44\nPurple = 45\nCyan = 46\nWhite = 47\n')
        b = int(b)
        c = int(c)
        d = int(d)

        def white_colorful_text(a,b,c,d):
            print('\033[{1};{2};{3}m {0} \033[0m'.format(a,b,c,d))
        white_colorful_text(a,b,c,d)

main()

# Old code below----------------------------------------------

# import sys


# def start_function():

    
#     if sys.argv[1] == 'RAINBOW':
#         rnbowlst = []
#         sys.stdout.write('\033[31mR\033[0m')
#         sys.stdout.write('\033[31mR\033[0m')
#         print('\n')
#     else:
#         a = input('What do you want to print? ')
#         b = input('What color do you want? ')
#         c = input('What kind of font/formatting do you want? ')
#         d = input('What kind of background do you want? ')
#         b = int(b)
#         c = int(c)
#         d = int(d)

#         def white_colorful_text(a,b,c,d):
#             print('\033[{1};{2};{3}m {0} \033[0m'.format(a,b,c,d))
#         white_colorful_text(a,b,c,d)




# start_function()











