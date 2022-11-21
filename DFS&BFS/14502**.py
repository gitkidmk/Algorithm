
# 벽을 세우고 -> 벽을 세우는 것은 collections으로
# BFS로 영역 넓이 확인하고
# 최대 영역 넓이 출력

from collections import deque
import copy
from itertools import combinations

def bfs(node):
    q = deque()

    for i in range(N):
        for j in range(M):
            if node[i][j] == 2:
                q.append((i,j,0))
    while q:
        i, j, k = q.popleft()
        if i not in range(N) or j not in range(M):
            continue
        if node[i][j] == 2 or (k == 1 and node[i][j] == 0):
            # 상하좌우 1이 아니면 (2또는 0이면) q에 추가
            node[i][j] = 3 # 방문처리는 3으로 한다
            q.append((i+1, j, 1))
            q.append((i-1, j, 1))
            q.append((i, j+1, 1))
            q.append((i, j-1, 1))
        elif node[i][j] == 1:
            node[i][j] = 3
            q.append((i+1, j, 0))
            q.append((i-1, j, 0))
            q.append((i, j+1, 0))
            q.append((i, j-1, 0))
    
    cnt = 0

    for i in range(N):
        cnt += node[i].count(0)

    return cnt
    
def wallCombi():
    zeros = []
    for i in range(N):
        for j in range(M):
            if node[i][j] == 0:
                zeros.append((i,j))
    
    return list(combinations(zeros, 3))
    




N, M = map(int, input().split())
node = []

for i in range(N):
    node.append(list(map(int, input().split())))

combi_results = wallCombi()

result = 0

for c in combi_results:
    node_t = copy.deepcopy(node)
    for cc in c:
        node_t[cc[0]][cc[1]] = 1
    zero_cnt = bfs(node_t)
    if zero_cnt > result:
        result = zero_cnt

print(result)

