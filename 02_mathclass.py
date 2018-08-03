#!/usr/bin/env python3

#Joshua Ching; Program will give you the Min, Max, Median, Mode, and Range of a given list
#Type your list in argv with a space between each number
#By Joching 
#-----------------------------------------------------------
import sys

def main():
    nums = sys.argv[1:]
    if len(nums) == 0:
        print(('\033[31mERROR: No values given\033[0m'))
        exit()

    for i in nums:
        i = int(i)

    nums = sorted(nums,key=int)

    #Min
    print (f'Min: {nums[0]}')
    #Max
    print(f'Max: {nums[-1]}')

    #mean
    count = 0
    total = 0
    for i in nums:
        total = total + int(i)
        count = count + 1

    mean_ans = total / count
    print(f'Mean: {mean_ans:.2f}')

    #Median
    _len = len(nums)
    if len(nums) % 2 == 0:#even
        med = (_len / 2 - 1)
        med2 = (_len / 2)
        med = int(med)
        med2 = int(med2)
        med3 = int(nums[med2]) + int(nums[med])
        med_ans = (med3 / 2) 
        #make "(med3 / 2)" an int for no float.
        
    else:#odd
        _len = int(_len)
        med_ans= _len // 2 + 1

    print(f'Median: {med_ans}') 

    #Mode
    no = 0
    q = 0

    for i in nums:
        if nums.count(i) > q:
            q = nums.count(i)
            no = i

    print(f'Mode: {no}')
        

    #Range
    if len(nums) == 1:# in case only 1 value given
        print(f'Range: {nums[0]}')
        exit()

    range_ans = int(nums[-1]) - int(nums[0])
    print(f'Range: {range_ans}')

main()