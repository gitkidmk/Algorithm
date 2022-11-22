import sys

def installC(dist):
    # dist만큼 혹은 이상 떨어진 house 위치 찾기
    count = 1
    lastLocate = house[0]
    i = 1
    while i < len(house):
        locate = house[i]
        if locate - lastLocate >= dist:
            count += 1
            lastLocate = locate
        i += 1

    return count

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
    if installC(mid) >= C:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)