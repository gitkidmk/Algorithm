#존재하면 1 아니면 0
def sol(num):
    # start end (index) 정의
    start = 0
    end = len(n_arr)-1
    
    # n_arr에서 num이 있는지 없는지 판단
    while start <= end:
        # mid 값 지정 : 내림 되는게 맞음
        mid = (start+end) // 2
        # if elif else
        if n_arr[mid] == num:
            return 1
        elif n_arr[mid] > num:
            end = mid-1
        else:
            start = mid+1
    return 0


n = int(input())
n_arr = list(map(int, input().split()))
n_arr = sorted(n_arr)

m = int(input())
m_arr = list(map(int, input().split()))

# start end mid

for num in m_arr:
    res = sol(num)
    print(res)
