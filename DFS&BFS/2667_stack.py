fourDir = [(1,0), (-1,0), (0,1), (0,-1)]

def dfs(graph, pos):
    x, y = pos
    stack = [(x, y)]
    count = 0
    while stack:
        p = stack.pop()
        x, y = p
        if graph[x][y] == 1:
            graph[x][y] = 0
            count += 1
            for dx, dy in fourDir:
                if x+dx in range(n) and y+dy in range(n):
                    stack.append((x+dx, y+dy))
    return count


# 이 때 graph는 이차원 배열인데, 0과 1로만 구성되어 있다. 이 때 0은 영역 아님, 1은 영역이다.
n = int(input())
graph = [[0]*n for _ in range(n)]

for i in range(n):
    row = str(input())
    for j in range(n):
        graph[i][j] = int(row[j])

village = 0
count = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            count.append(dfs(graph, (i,j)))
            village += 1
print(village)

count.sort()

for c in count:
    print(c)