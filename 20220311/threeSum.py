import string
import collections
from pprint import pprint


def threesum():
    nums = [-1, 0, 1, 2, -1, -4]

    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        #중복값 건너뛰기
        if i > 0 and nums[i] == nums[i-1]:
            continue

    left, right = i+1, len(nums) - 1
    while left < right:
        sum = nums[i] + nums[left] + nums[right]
        if sum < 0:
            left += 1
        elif sum > 0:
            right -= 1
        else:
            results.append([nums[i], nums[left], nums[right]])


            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1
            left += 1
            right -= 1

    return results
    ## two point start and end


def threesum2(nums):
    nums.sort()
    result = []
    pprint(len(nums)-2)
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l = i+1
        r = len(nums)-1

        while(l<r):
             sum = nums[i] + nums[l] + nums[r]
             if sum<0:
               l+=1
             elif sum >0:
               r-=1
             else:
               result.append([nums[i],nums[l],nums[r]])
               while l<len(nums)-1 and nums[l] == nums[l + 1] : l += 1
               while r>0 and nums[r] == nums[r - 1]: r -= 1
               l+=1
               r-=1
    return result

pprint(threesum2([-1, 0, 1, 2, -1, -4]))
