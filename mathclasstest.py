# import sys

# nums = sys.argv[1:]

# for i in nums:
#     i = int(i)


# nums = sorted(nums,key=int)


#!/usr/bin/env python3

#Joshua Ching; Word is 
#By Joching 



import random
import time

def main():
    wordlist = ['Happy','Funny','Dance','China','Water','Tiger','Phone','Candy','Cards','Boats','Kites']
    secret = random.choice(wordlist)
    print(f'The secret word begins with a {secret[0]}')
    secret = secret.lower()

    time_start = time.time()
    count = 9#--------------------------Guesses

    while count <10:
        answer = input()
        answer = answer.lower()
        if answer == '':
            print('You wasted a guess!')
        elif answer[0] != secret[0] and len(answer) == 5:
            print('ABCDEFJHIJKLMNOPQRSTUVWXYZ')
        elif len(answer) != 5:
            print("0,1,2,3,4 that's how we count to five!")
        elif answer == secret:
            t, m = timer(time_start)
            print('*'*54)
            print('*',f'\033[32mYOU WIN\033[0m'.center(59),'*')
            print('*',f'You won in only {m:.0f} minute(s) and {t:.0f} second(s)'.center(50),'*')
            print('*'*54)
            quit()
        elif answer[0] == secret[0] and answer != secret and len(answer) == 5:
            count += 1
            print(f'You have {10 - count} guesses left!')



    if count is 10:
        t, m = timer(time_start)
        print('*'*54)
        print('*','\033[31mGAME OVER\033[0m'.center(59),'*')
        print('*', f'The word was: {secret}'.center(50),'*')
        print('*',f'You lost in a mere {m:.0f} minute(s) and {t:.0f} second(s)'.center(50),'*')
        print('*'*54)



def timer(time_start):
    t, m = 0,0
    t = time.time() - time_start
    m = t // 60
    t = t % 60
    return t, m

main()