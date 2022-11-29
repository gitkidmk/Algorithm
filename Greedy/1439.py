# flag 설정
# loop -> arr 값 갱신
# arr의 최소값 뽑기

s=input()

flag = 0

if s[0] == '0':
    flag = 1

arr = [0,0]

for ss in s:
    if ss == '0' and flag == 1:
        arr[0] += 1
        flag = 0
    if ss == '1' and flag == 0:
        arr[1] += 1
        flag = 1

print(min(arr))