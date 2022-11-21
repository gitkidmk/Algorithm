# 재귀에서 recusrion error -> 반복문으로 변경
from collections import deque

def main():
    N = int(input())
    network = [tuple(map(int, input().split())) for _ in range(0,N-1)]
    g = [[] for _ in range(N+1)]
    p_nodes = [0 for _ in range(N+1)]
    p_nodes[1] = 1 # 1 node의 부모는 1이라고 한다

    # create network relation
    for a, b in network:
        g[a].append(b)
        g[b].append(a)

    q = deque()
    q.append(1)
    while q:
        node = q.popleft()
        for n in g[node]:
            if p_nodes[n] == 0:
                p_nodes[n] = node
                q.append(n)
    


    for i in range(2,N+1):
        print(p_nodes[i])
    


if __name__ == "__main__":
    main()