N = str(input())
arr = list(map(int, N))

arr.sort(reverse=True)

result = ''.join(map(str, arr))

print(result)