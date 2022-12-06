import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
a.insert(0,0)

d=[0]*(n+1)

d[1] = a[1]

dp_arr = []

for i in range(2,n+1):
    for j in range(i-1,int(i/2)-1,-1):
        dp_arr.append(d[j]+d[i-j])

    dp_max = max(dp_arr)
    d[i] = max(a[i], dp_max)

print(d[-1])