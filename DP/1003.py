N = int(input())
arr = [[0,0] for _ in range(41)]
arr[0] = [1,0]
arr[1] = [0,1]
for _ in range(N):
    n = int(input())
    if n < 2 :
        print(arr[n][0], arr[n][1])
    else:
        for i in range(2,n+1):
            arr[i] = [arr[i-1][0]+arr[i-2][0], arr[i-1][1]+arr[i-2][1]]
        print(arr[i][0], arr[i][1])
