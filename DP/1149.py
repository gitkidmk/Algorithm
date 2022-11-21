'''
3
26 40 83
49 60 57
13 89 99
'''

import copy


N = int(input())

house = [[]] * (N+1)
minIndex = [-1] * (N+1)

result = 0

for i in range(1,N+1):
    arr = list(map(int, input().split()))
    minVal = min(arr)
    idx = arr.index(minVal)
    result += minVal
    house[i] = arr
    minIndex[i] = idx
print(house, minIndex)


for i in range(2,N):
    tHouse = copy.deepcopy(house)
    if minIndex[i] == minIndex[i-1] == minIndex[i+1]:
        print("연구필요",i)
        idx = minIndex[i]
        bef = tHouse[i][idx]
        del tHouse[i][idx]
        aft = min(tHouse[i])
        minIndex[i] = house.index(aft)
        result -= bef
        result += aft

for i in range(3,N-1):
    tHouse = copy.deepcopy(house)
    if minIndex[i] == minIndex[i-1]:
        idx = minIndex[i]
        # i = a, i-1 = b
        s = minIndex[i] + minIndex[i+1]
        aIdx = 0
        if s == 1:
            aIdx = 2
        elif s == 2:
            aIdx = 1
        s = minIndex[i-1] + minIndex[i-2]
        bIdx = 0
        if s == 1:
            bIdx = 2
        elif s == 2:
            bIdx = 1
        aResult = result - house[i][idx] + house[i][aIdx]
        bResult = result - house[i-1][idx] + house[i-1][bIdx]
        if aResult > bResult:
            result = bResult
            minIndex[i-1] = bIdx
        else:
            result = aResult
            minIndex[i] = aIdx
if minIndex[1] == minIndex[2]:
    tHouse = copy.deepcopy(house)
    idx = minIndex[1]
    del tHouse[1][idx]
    aMin = min(tHouse[1])
    del tHouse[2][idx]
    del tHouse[2][minIndex[3]]
    bMin = tHouse[2][0]
    aVal = house[1][idx]
    bVal = house[2][idx]
    aResult = result - aVal + aMin
    bResult = result - aVal + aMin
    result = aResult
    if aResult > bResult:
        result = bResult


if minIndex[N-1] == minIndex[N]:
    tHouse = copy.deepcopy(house)
    idx = minIndex[N]
    del tHouse[N][idx]
    aMin = min(tHouse[N])
    del tHouse[N-1][idx]
    del tHouse[N-1][minIndex[N-2]]
    bMin = tHouse[N-1][0]
    aVal = house[N][idx]
    bVal = house[N-1][idx]
    aResult = result - aVal + aMin
    bResult = result - aVal + aMin
    result = aResult
    if aResult > bResult:
        result = bResult


print(result)


'''

    elif minIndex[i] != minIndex[i-1] and minIndex[i] != minIndex[i+1]:
        continue
    else:
        idx1= bef1= idx2= bef2= aft1= aft2 = 0
        if minIndex[i] == minIndex[i+1]:
            idx1 = minIndex[i]
            bef1 = tHouse[i][idx1]
            idx2 = minIndex[i+1]
            bef2 = tHouse[i+1][idx2]
            del tHouse[i][idx1]
            del tHouse[i+1][idx2]
            aft1 = min(tHouse[i])
            aft2 = min(tHouse[i+1])
        else:
            idx1 = minIndex[i]
            bef1 = tHouse[i][idx1]
            idx2 = minIndex[i-1]
            bef2 = tHouse[i-1][idx2]
            del tHouse[i][idx1]
            del tHouse[i-1][idx2]
            aft1 = min(tHouse[i])
            aft2 = min(tHouse[i-1])
        if aft1 - bef1 > aft2 - bef2:
            minIndex[i] = house.index(aft)
            result -= bef2
            result += aft2
        else:
            result -= bef1
            result += aft1
'''
