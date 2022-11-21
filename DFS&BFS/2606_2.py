def dfs(node, g, v):
    # node가 방문했던 놈인지 확인 - 방문안했으면 로직 진행, 방문처리
    if v[node] == False:
        v[node] = True
        for n in g[node]:
            dfs(n, g, v)
    return v

def main():
    N = int(input())
    nw_count = int(input())

    # [[],[], ... []] : 노드 개수 + 1 만큼의 이차원 배열 생성, 각 노드의 index는 노드 number와 일치
    g = [[] for _ in range(N+1)]
    v = [False for _ in range(N+1)]

    for _ in range(nw_count):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    answer = dfs(1, g, v)

    answer = answer.count(True)-1

    print(answer) # v의 True 개수
    return answer

if __name__ == "__main__":
    main()


