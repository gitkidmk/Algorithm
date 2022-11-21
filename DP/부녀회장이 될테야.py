N = int(input())

for _ in range(N):
    k = int(input())
    n = int(input())
    f = [[0] * 15 for _ in range(15)]
    
    # 0층 인원수 넣기
    for i in range(1,15):
        f[0][i] = i
    
    # k층 n호 인원 계산
    for o in range(1, k+1):
        for p in range(1, n+1):
            for q in range(1, p+1):
                f[o][p] += f[o-1][q]
    
    print(f[k][n])
    