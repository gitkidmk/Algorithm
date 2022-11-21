N = int(input())
A = list(map(int, input().split()))
subA = [A[0]]
lenA = len(A)

for i in range(1,lenA):
    # goal: subA에 값 하나씩 채워넣기
    # subA 마지막 원소보다 크면 subA에 append
    # 아니면 적절한 위치를 이분탐색으로 찾기
    if subA[-1] < A[i]:
        subA.append(A[i])
    else:
        left = 0
        right = len(subA) - 1
        while left < right:
            mid = (left + right)//2
            if subA[mid] < A[i]:
                left = mid + 1
            else:
                right = mid
        subA[right] = A[i]
print(len(subA))