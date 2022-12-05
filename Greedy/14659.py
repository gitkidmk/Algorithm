# 배열 받기
# 오른쪽이 본인보다 높으면 break
# 오른쪽이 본인보다 낮으면 count += 1

from sys import stdin

n = int(input())
arr = list(map(int, stdin.readline().split()))

flag = 0
answer = 0

while flag < n-1:
    cnt = 0
    for i in range(flag+1,n):
        if (arr[flag] > arr[i]):
            cnt += 1
        else:
            break
    flag += 1
    if answer < cnt:
        answer = cnt
    if answer > n-flag:
        break

print(answer)

