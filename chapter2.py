import string
import collections
from pprint import pprint


def towsum():
    nums = [2,7,11,15]
    target = 9

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                print(i,j)

def towsum2():
    nums = [2,7,11,15]
    target = 9

    for i, n in enumerate(nums):
        pprint(n )

            



towsum2()


