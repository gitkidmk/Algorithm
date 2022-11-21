# 그 안의 인자 수 까지 count

fourDir=[(1,0),(-1,0),(0,1),(0,-1)]

def dfs(g,x,y):
    s = [(x,y)]
    cnt = 0
    while s:
        px, py = s.pop()
        if g[px][py]==1:
            g[px][py]=0
            cnt += 1
            # 상하좌우 움직이기
            for dx, dy in fourDir:
                if px+dx in range(m) and py+dy in range(n):
                    s.append((px+dx, py+dy))
    return cnt

T=int(input())

for _ in range(T):
    m,n,k = map(int, input().split())
    g=[[0]*n for _ in range(m)]
    for _ in range(k):
        x,y = map(int, input().split())
        g[x][y] = 1

    # cnt : 영역 cnt    
    cnt = 0
    for i in range(m):
        for j in range(n):
            if g[i][j]==1:
                itemCnt = dfs(g,i,j)
                cnt += 1
                print("itemCnt: ",itemCnt)
    print(cnt)