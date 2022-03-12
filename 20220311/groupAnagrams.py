import string
import collections
from pprint import pprint

#혼자 풀기 
def groupanagrams():
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
