import string
import collections
from pprint import pprint



def biggestNum() :
    text = 'hello, this is sparta'

    counter = {} #딕셔너리
    for char in text:
        if not char.isalpha():
            continue
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

    pprint(counter)




def checkingLetter():
    for lo in string.ascii_lowercase:
        for char in text:
            if lo == char:
                if lo in counter2:
                    counter2[lo] += 1
                else:
                    counter2[lo] = 1
    pprint(counter2)





def alphabetlocation():
    text = 'beakjoon'
    dic = [] 

    for char in text:
        if char in string.ascii_lowercase:
            pprint(string.ascii_lowercase.index(char))


    for lo in text:
        for char in string.ascii_lowercase:
            if lo == char:
                dic.append(string.ascii_lowercase.index(lo))
        dic.append(-1) 

    
    print(dic)


## 첫번째 문제
def groupAnagrams():
    strs = ["eat","tea","tan","ate","nat","bat"]

    ##예외 처리
    if len(strs[1]) == 0:
        return [[""]]
    if len(strs[1]) == 1:
        return [[strs[1]]]

    
    sorted_strs = collections.defaultdict(list)

    data = [0 for i in range(len(strs))]
    dic = {}
    result = []

    for i in range(len(strs)):
        for j in range(len(strs[i])):
            pprint(ord(strs[i][j])) 
            data[i] += (ord(strs[i][j]))
        dic = {strs[i]:data[i] for i in range(len(strs))}
        pprint("-----------")

    dic = sorted(dic.items(), key=lambda x: x[1])
    pprint(dic)


    result = [] 
    for value in data:
        if value not in result:
            result.append(value)
            
    result2 = []


    pprint(result2)
    print(result)
#sorting


def longestPalindome():
    text = 'bananas'

    if len(text) == 1:
        return 1
    if len(text) == 2:
        return 2

    x = list(text) 

    result = []
    dic = {}

    ##중복값 찾는 for문
    for value in x:
        if value not in result:
            result.append(value)

    
    #각 알파벳의 개수를 딕셔너리로 저장한다
    for i in x:
        if i in result:
            dic = {i:x.count(i) for i in result}

    odd = []
    result = []


    #홀수 찾기가장 큰 값찾기
    for i in dic:
        if dic[i] % 2 == 1:
            odd.append(dic[i])  ##홀수만 따로 계산 
        elif dic[i] % 2 == 0:
            result.append(dic[i]) ##짝수는 바로넣는다 


    
    pprint(odd)
    pprint(result)
    if not odd:
        return sum(result)
    else:
        maxValue = odd[0]

    for i in range(0, len(odd)):
        if maxValue < odd[i]:
            maxValue = odd[i]
            result.append(odd[i]-1)
    result.append(maxValue)

    pprint(result)
    return sum(result)
    







def longestPalindrome():
    s = 'babad'
    dic = {}

    for i in range(len(s)):
        if s[i] in dic:
            dic[s[i]] += 1
        else:
            dic[s[i]] = 1
    check = False
    pprint(dic)

    li = []
    for counting in dic :
        if dic[counting] % 2 == 0:
            check = True
        li.append(dic[counting])
    pprint(li)

    res = 0
    for i in range(len(li)):
        pprint(li[i] )
        pprint("---------")

        pprint(li[i] % 2)
        res += li[i] - (li[i] % 2)
    return res if check == False else res+1




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


