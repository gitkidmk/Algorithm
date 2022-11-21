# 1931

# (a,b)를 a 기준으로 정렬 + b기준으로 정렬
N = int(input())
arr = []
for _ in range(N):
    l, r = tuple(map(int, input().split()))
    arr.append((l,r))
arr.sort()
arr.sort(key=lambda x: x[1])

cnt = 1
a, b = arr[0]
for i in range(1,N):
    c, d = arr[i]
    if b <= c:
        b = d
        cnt += 1
print(cnt)