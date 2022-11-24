s = int(input())

ans = 0
n = 0
while True:
    a = s - n*(n+1)/2
    if a == 0:
        ans = n
        break
    if a > n:
        ans = n+1
    else:
        break
    n += 1
print(ans)