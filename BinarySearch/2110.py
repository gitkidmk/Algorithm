# 여러 줄 input으로 받고자 할때 input()을 지양하고
# sys.stdin.readline()을 지향하자
# propmpt message, buffer와 같은 이유로 sys가 효율성 더 좋음

import sys

def installC(dist):
    # dist만큼 혹은 이상 떨어진 house 위치 찾기 by Binary Search
    # left right는 house 인덱스
    left = 0
    right = len(house) - 1
    target = house[left] + dist # dist만큼 떨어진 위치
    cnt = 1

    while target <= house[-1]:
        while left < right:
            mid = (left + right)//2
            if house[mid] < target:
                left = mid + 1
            else:
                right = mid
        target = house[right] + dist
        left = right
        right = len(house) - 1
        cnt += 1
        if cnt >= C:
            return True
    return False


N, C = map(int, input().split())
house = []
for _ in range(N):
    # house.append(int(input()))
    house.append(int(sys.stdin.readline()))

house.sort()

left = 1
right = house[-1]-house[0]
answer = 0

while left <= right:
    mid = (left + right)//2
    if installC(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)