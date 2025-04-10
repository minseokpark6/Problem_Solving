import sys
# 입력
n = int(input())
# 계수 정렬 >> Counting Sort: 인덱스로 접근 
# O(n)의 시간 복잡도로 접근 
arr = [0] * 10001

# 입력되는 숫자의 인덱스 값을 1로 변경 
for _ in range(n):
    idx = int(sys.stdin.readline())
    arr[idx] += 1
    
# 출력 
for i in range(1, 10001):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)

''' 오답 >> 메모리 초과 >> 리스트에 모든 숫자를 하나하나 저장한 후 출력하는 형태
import sys
# 입력
n = int(input())
arr = sorted([int(sys.stdin.readline()) for _ in range(n)])
# 출력
print(*arr, sep='\n')
'''