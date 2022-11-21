fourDir = [(1,0),(-1,0),(0,1),(0,-1)]

def dfs(g,v,s):
    global fourDir
    while s:
        (nx, ny) = s.pop()
        if g[nx][ny] == 1 and v[nx][ny] == False: # 배추이고, 방문한적 없다면
            v[nx][ny] = True
            for dx, dy in fourDir:
                if nx+dx in range(0,m) and dy+dy in range(0,n):
                    s.append((nx+dx, ny+dy))
            # print("nx ny is ...", nx, ny)
            return True
        else:
            return False


N = int(input())
for _ in range(N):
    m, n, k = map(int, input().split())
    # k 만큼의 loop 돌면서 g 만들기
    g = [[0] * n for _ in range(m)] # m * n g with 0
    v = [[False] * n for _ in range(m)] # 방문여부
    for _ in range(k):
        a,b = map(int, input().split())
        g[a][b] = 1
    
    s = []
    s.append((0,0))

    dfs(g,v,s)
    # print(dfs(g,v,s))

    s = []
    cnt = 0

    for i in range(m):
        for j in range(n):
            s.append((i,j))
            if dfs(g,v,s) == True:
                cnt +=1
    print("cnt: ",cnt)

