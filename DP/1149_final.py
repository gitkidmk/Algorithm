import sys

n = int(input())

arr = [[] for _ in range(n+1)]
d = [[0,0,0] for _ in range(n+1)]


for i in range(1,n+1):
    arr[i] = list(map(int, sys.stdin.readline().split()))

for i in range(1, n+1):
    d[i][0] = min(d[i-1][1],d[i-1][2])+arr[i][0]
    d[i][1] = min(d[i-1][0],d[i-1][2])+arr[i][1]
    d[i][2] = min(d[i-1][1],d[i-1][0])+arr[i][2]

answer = min(d[n][0], d[n][1], d[n][2])
print(answer)