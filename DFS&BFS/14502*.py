
# 벽을 세우고 -> 벽을 세우는 것을 재귀로 돌리면서 
# BFS로 영역 넓이 확인하고
# 최대 영역 넓이 출력

from collections import deque
import copy

result = 0

def bfs():
    global result
    q = deque()
    node_t = copy.deepcopy(node)

    for i in range(N):
        for j in range(M):
            if node_t[i][j] == 2:
                q.append((i,j,0))
    while q:
        i, j, k = q.popleft()
        if i not in range(N) or j not in range(M):
            continue
        if node_t[i][j] == 2 or (k == 1 and node_t[i][j] == 0):
            # 상하좌우 1이 아니면 (2또는 0이면) q에 추가
            node_t[i][j] = 3 # 방문처리는 3으로 한다
            q.append((i+1, j, 1))
            q.append((i-1, j, 1))
            q.append((i, j+1, 1))
            q.append((i, j-1, 1))
    
    cnt = 0

    for i in range(N):
        cnt += node_t[i].count(0)

    result = max(result, cnt)
    


def createWall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if node[i][j] == 0:
                node[i][j] = 1
                createWall(cnt+1)
                node[i][j] = 0



N, M = map(int, input().split())
node = []

for i in range(N):
    node.append(list(map(int, input().split())))

createWall(0)


print(result)

