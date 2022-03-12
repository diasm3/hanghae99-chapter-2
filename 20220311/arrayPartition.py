import string
import collections
from pprint import pprint


def arraypartition(nums):
    sum = 0 
    pair = []
    nums.sort()

    for n in nums:
        pair.append(n)
        if len(pair) ==2:
            sum += min(pair)
            pair = []

    return sum


pprint(arraypartition([6,2,6,5,1,2]))

 


