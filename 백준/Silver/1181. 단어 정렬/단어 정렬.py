# 단어 개수 입력
n = int(input())
# 단어 입력 및 오름차순 정리
arr = sorted(set([input() for _ in range(n)]), key= lambda x:(len(x), x))
# 출력
print(*arr, sep='\n')