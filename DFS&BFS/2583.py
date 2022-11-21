def dfs(i,j,node):
    stack = [(i,j)]
    cnt = 0
    while stack:
        i,j = stack.pop()

        if i not in range(N) or j not in range(M):
            continue
        if node[i][j] == 0:
            node[i][j] = 1
            cnt += 1

            # 상하좌우 관련해서 colored에 넣기
            stack.append((i+1, j))
            stack.append((i-1, j))
            stack.append((i, j+1))
            stack.append((i, j-1))

    return cnt



M,N,K = map(int, input().split())
node = [[0]*M for _ in range(N)]
filled = set()
for i in range(K):
    a,b,c,d = map(int, input().split())
    for i in range(a,c):
        for j in range(b,d):
            filled.add((i,j))
for f in filled:
    node[f[0]][f[1]] = 1

area = 0
result = []

for i in range(N):
    for j in range(M):
        if node[i][j] == 0:
            r = dfs(i,j,node)
            area += 1
            result.append(r)

result.sort()
print(area)
print(' '.join(list(map(str, result))))

