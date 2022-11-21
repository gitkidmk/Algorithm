# 재귀에서 recusrion error -> 반복문으로 변경

def dfs(node, g, p_nodes):
    for n in g[node]:
        # 방문 안했어, 로직 돌아
        if p_nodes[n] == 0:
            p_nodes[n] = node
            dfs(n, g, p_nodes)

def main():
    N = int(input())
    network = [tuple(map(int, input().split())) for _ in range(0,N-1)]
    g = [[] for _ in range(N+1)]
    p_nodes = [0 for _ in range(N+1)]

    # create network relation
    for a, b in network:
        g[a].append(b)
        g[b].append(a)

    # with dfs loop, create parent node g
    # 방문 여부는 해당 칸이 0이 아니면 방문한 것
    dfs(1, g, p_nodes)
    for i in range(2,N+1):
        print(p_nodes[i])


if __name__ == "__main__":
    main()