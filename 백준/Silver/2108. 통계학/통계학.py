import sys
from collections import Counter
input = sys.stdin.readline
# 입력 
n = int(input())
arr = sorted([int(input()) for _ in range(n)])
# 산술평균 구하기
mean = round(sum(arr)/len(arr))
# 중앙값 구하기
median = arr[(len(arr)//2)]
# 촤빈값 구하기
dic = sorted(Counter(arr).items(), key=lambda x: (-x[1], x[0]))
if len(dic) == 1:
    mode = dic[0][0]
    # 최빈값이 여러 개 일 경우
else:
    if dic[0][1] == dic[1][1]:
        mode = dic[1][0]
    # 최빈값이 하나일 경우
    else:
        mode = dic[0][0]
# 범위 구하기
freq = arr[-1]-arr[0]

# 출력 
print(mean)
print(median)
print(mode)
print(freq)