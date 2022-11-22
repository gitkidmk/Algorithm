import sys

def installC(dist):
    # dist만큼 혹은 이상 떨어진 house 위치 찾기
    count = 1
    lastLocate = house[0]

    for i in range(1,len(house)):
        locate = house[i]
        if locate - lastLocate >= dist:
            count += 1
            lastLocate = locate
    return count

def binarySearch(house, C):
    left = 1
    right = (house[-1]-house[0])//(C-1)
    answer = 0

    while left <= right:
        mid = (left + right)//2
        cnt = 1
        cur = house[0]
        for i in range(1, len(house)):
            if house[i] - cur >= mid:
                cnt +=1
                cur = house[i]
        if cnt >= C:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer


N, C = map(int, input().split())
house = []
for _ in range(N):
    house.append(int(sys.stdin.readline()))
house.sort()

answer = binarySearch(house, C)
print(answer)