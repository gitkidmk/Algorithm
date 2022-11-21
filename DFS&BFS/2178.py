from collections import deque

def bfs():
    ans = 0
    q = deque()
    # x, y, cnt
    q.append((0,0,0))

    while q:
        i, j, cnt = q.popleft()
        if i not in range(N) or j not in range(M):
            continue
        if i == N-1 and j == M-1:
            ans = cnt + 1
            break
        if node[i][j] == 1:
            cnt += 1
            node[i][j] = 2
            q.append((i+1, j, cnt))
            q.append((i-1, j, cnt))
            q.append((i, j+1, cnt))
            q.append((i, j-1, cnt))
    return ans

N, M = map(int, input().split())

node = []
for i in range(N):
    node.append(list(map(int, input())))

ans = bfs()
print(ans)
