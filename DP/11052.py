def dp(N,i):
    return N//i * arr[i] + max_result[N%i]


N = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)

max_result = [0]*(N+1)

for i in range(1,N+1):
    dp_list = []
    for j in range(1, i+1):
        a = dp(i,j)
        dp_list.append(a)
    max_result[i] = max(dp_list)
print(max_result[-1])