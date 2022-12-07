import sys

def dfs(node):
    stack = [node]
    while stack:
        n = stack.pop()
        if visited[n] == False:
            visited[n] = True
            for g in graph[n]:
                stack.append(g)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

count = 0
for i in range(1,n+1):
    if visited[i] == False:
        dfs(i)
        count += 1
print(count)