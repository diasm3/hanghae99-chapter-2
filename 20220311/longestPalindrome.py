import string
import collections
from pprint import pprint

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

