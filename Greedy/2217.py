import sys

N = int(input())

rope = [int(sys.stdin.readline()) for _ in range(N)]
rope.sort()

answer = []
# 가장 앞의 rope를 제거하면서 rope[-1]보다 크면 저장한다
for i in range(len(rope)):
    w = (len(rope)-i)*rope[i]
    if w >= rope[-1]:
        answer.append(w)
print(max(answer))