# 보석 쇼핑
# 효율성 실패....

# dictionary copy할때 deepcopy 잊지말기
from copy import deepcopy

def findByLen(mid, gems, getDict):
    # ??? parameter에서 gems 뺄 수 있나?
    sub_gems = gems[0:mid]
    dict = deepcopy(getDict)
    for item in sub_gems:
        dict[item] += 1
    # dict의 value가 모두 1 이상
    if list(dict.values()).count(0) == 0:
        return [1, mid]
    
    for i in range(1, len(gems)-mid+1):
        dict[gems[i-1]] -= 1
        dict[gems[mid+i-1]] += 1
        # dict의 모든 values가 1 이상일때로 수정
        if list(dict.values()).count(0) == 0:
            return [i+1, i+mid]
    return [0, 0]

def solution(gems):
    answer = []
    # gem set 만들기
    getDict = {gems[i]: 0 for i in range(len(gems))}
    # sub_gems 길이에 대한 binary search 생성
    left = len(getDict)
    right = len(gems)
    while left <= right:
        mid = (left+right)//2
        subGemExist = findByLen(mid,gems,getDict)
        if subGemExist == [0,0]:
            left = mid + 1
        else:
            right = mid - 1
            answer = subGemExist
    return answer