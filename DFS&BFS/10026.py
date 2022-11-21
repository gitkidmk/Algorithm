def dfs(i,j,node):
    p_color = node[i][j]
    colored = [(i,j)]
    result = 0
    cnt = 0
    while colored:
        cnt += 1
        i,j = colored.pop()

        if i not in range(0,N) or j not in range(0,N):
            continue
        if node[i][j] == p_color:
            node[i][j] = 'C'
            result += 1
            # 상하좌우 관련해서 colored에 넣기
            colored.append((i+1, j))
            colored.append((i-1, j))
            colored.append((i, j+1))
            colored.append((i, j-1))
    return result

N = int(input())

node = [[0]*N for _ in range(N)]
node_p = [[0]*N for _ in range(N)]

# input 넣기
for i in range(N):
    line = str(input())
    for j in range(N):
        node[i][j] = line[j]

# input rg 넣기
for i in range(N):
    for j in range(N):
        if node[i][j] == 'R' or node[i][j] == 'G':
            node_p[i][j] = 'P'

area = 0
area_p = 0
# RGB C(Checked)
for i in range(N):
    for j in range(N):
        if node[i][j] != 'C':
            a = dfs(i,j,node)
            area += 1
        if node_p[i][j] != 'C':
            b = dfs(i,j,node_p)
            area_p += 1
print(area, area_p)