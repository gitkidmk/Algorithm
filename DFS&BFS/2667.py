# DFS
# print 출력은 하나만 해서 제출

def visitedCount(v):
    cnt = 0
    for i in range(len(v)):
        for j in range(len(v)):
            if v[i][j] == True:
                cnt += 1
    return cnt

def dfs(G, i, j, v):
    # 1이라면, 방문 여부 확인 > 방문
    if G[i][j] == 1 and v[i][j] == False:
        v[i][j] = True
        for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
            # 범위 내라면
            if i+di in range(len(v)) and j+dj in range(len(v)):
                dfs(G, i+di, j+dj, v)
    return visitedCount(v)
        


def main():
    N = int(input())
    G = [[] for _ in range(N)]
    v = [[] for _ in range(N)]
    for i in range(N):
        row = str(input())
        for j in range(N):
            G[i].append(int(row[j]))
            v[i].append(False)
    
    answer = []
    cnt = 0
    for i in range(N):
        for j in range(N):
            if G[i][j] == 1 and v[i][j] == False:
                c = dfs(G, i, j, v)
                answer.append(c-cnt)
                cnt = c
    answer.sort()
    print(len(answer))
    for a in answer:
        print(a)

if __name__ == "__main__":
    main()