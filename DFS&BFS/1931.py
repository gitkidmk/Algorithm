# 1931

# (a,b)를 a 기준으로 정렬
N = int(input())
arr = []
for _ in range(N):
    l, r = tuple(map(int, input().split()))
    arr.append((l,r))

arr.sort()

# 전체 탐색
# 현재 생성한 조합이 기존 조합의 부분집합이면 break
start = 0
pos_group = []
max_len = 0
flag = False
# 시작 인덱스를 증가시키면서 while 진행
while start < N:
    # 시작 인덱스는 무조건 pos_arr에 담는다 then 가능한 조합 pos_arr에 담기
    pos_arr = [arr[start]]
    for i in range(start+1, N):
        c, d = pos_arr[-1]
        a, b = arr[i]
        if a >= d:
            pos_arr.append((a,b))
    
    # 최대값 갱신        
    if len(pos_arr) >= max_len:
        max_len = len(pos_arr)

    # pos_arr를 집합 형태로 전환해 기존의 pos_group에 있는지 확인
    for pos_group_set in pos_group:
        if set(pos_arr) < pos_group_set:
            flag = True
    
    # 기존 조합의 부분집합이면 더 볼 필요 없음
    if flag == True or N-start < max_len:
        break
    
    pos_group.append(set(pos_arr))
    start += 1

print(max_len)
