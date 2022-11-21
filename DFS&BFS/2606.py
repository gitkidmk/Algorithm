def dfs(node, g, v):
    #방문 안했으면 방문처리하고 돈다
    if v[node] == 0:
        #방문처리
        v[node] = 1
        #g에서 node를 포함하는 상대 노드에 dfs 돈다
        for a,b in g:
            if a == node:
                dfs(b, g, v)
            elif b == node:
                dfs(a, g, v)
            else:
                continue
    return v

def main():
    N = int(input())
    g_len = int(input())

    g = []
    for _ in range(g_len):
        a, b = map(int, input().split())
        g.append((a,b))
    v = {i:0 for i in range(1,N+1)}
    
    v = dfs(1,g,v)
    
    count = -1

    for vv in v.values():
        if vv == 1:
            count += 1
    print(count)
    return count

    


if __name__ == "__main__":
    main()