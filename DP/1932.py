import sys

n = int(input())

arr = [[] for _ in range(n+1)]
d = [[0]*i for i in range(n+1)]

for i in range(1,n+1):
    arr[i] = list(map(int,sys.stdin.readline().split()))

d[1][0] = arr[1][0]

for m in range(2,n+1):
    for i in range(m):
        if i == 0:
            d[m][i] = d[m-1][i] + arr[m][i]
        elif i == m-1:
            d[m][i] = d[m-1][i-1] + arr[m][i]
        else:
            d[m][i] = max(d[m-1][i-1],d[m-1][i]) + arr[m][i]
print(max(d[-1]))
