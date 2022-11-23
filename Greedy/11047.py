from sys import stdin

N, K = map(int, input().split())

coin = [int(stdin.readline()) for _ in range(N)]

# K를 큰 coin 부터 차례로 몫을 취하고, 몫이 있으면 동전 개수에 더한다
# K는 몫을 취한 값을 빼고 진행한다

answer = 0

for i in range(len(coin)-1, -1, -1):
    if K == 0:
        break
    share = K//coin[i]
    answer += share
    K -= coin[i]*share
print(answer)