# 파이썬으로 풀고, java로도 풀어보자
# 파이썬 이차원 배열에 대한 이해도 재정립 필요
# BFS, DFS에서 항상 방문여부를 먼저 확인하는 폼 정립 필요

import sys
import copy
from collections import deque

def dfs(n):
    nodes_d = copy.deepcopy(nodes)
    for node in nodes_d:
        node.sort(reverse=True)
    
    visited = [0 for _ in range(n+1)]
    answer = []
    stack = deque([v])
    while stack:
        node = stack.pop()
        if visited[node] == 0:
            visited[node] = 1
            answer.append(node)
            for n in nodes_d[node]:
                stack.append(n)
    
    print(' '.join(map(str, answer)))
        

def bfs(n):
    nodes_b = copy.deepcopy(nodes)
    for node in nodes_b:
        node.sort()
    visited = [0 for _ in range(n+1)]
    answer = []
    queue = deque([v])
    while queue:
        node = queue.popleft()
        if visited[node] == 0:
            visited[node] = 1
            answer.append(node)
            for n in nodes_b[node]:
                queue.append(n)
    
    print(' '.join(map(str, answer)))



n, m, v = map(int, input().split())

nodes = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    nodes[a].append(b)
    nodes[b].append(a)

dfs(n)
bfs(n)