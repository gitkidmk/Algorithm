N = int(input())

f = [0]*1001

f[1] = 1
f[2] = 2

if N < 3:
    print(f[N])
else:
    for i in range(3,N+1):
        f[i] = f[i-1] + f[i-2]
    print(f[i]%10007)