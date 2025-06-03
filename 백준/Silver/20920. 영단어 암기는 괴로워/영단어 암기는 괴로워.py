import sys
from collections import Counter
input = sys.stdin.readline
# 입력 
n, m = map(int, input().split())
# 길이가 m 이상인 단어 리스트
arr = [word for _ in range(n) if len((word := input().strip())) >= m]
# 우선 순위 지정
dic = dict(Counter(arr))
sorted_dic = sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
# (-x[1], -len(x[0]), x[0]) >> 순서 별로 우선순위 지정 
# 1) -x[1]: 단어의 개수 별 내림차순 
# 2) -len(x[0]) : 단어 길이 별 내림차순 
# 3) x[0] : 단어 알파벳 순 오름차순 정렬 

# 출력 
for i in sorted_dic:
    print(i[0])