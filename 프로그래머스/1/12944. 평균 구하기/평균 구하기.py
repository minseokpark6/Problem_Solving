def solution(arr):
    return sum(arr) / len(arr)

''' 
파이썬에서 평균을 구하는 가장 효율적인 방법 

(1) sum(arr) / len(arr)

(2) numpy 활용
numpy.mean(arr)

-> 대용량 데이터에 더 적합한 방법 
-> 데이터 용량이 적을 경우 오히려 import하는 메모리가 더 소모됨.
'''


'''
## 이전 코드 

def solution(arr):
    answer = sum(arr) / len(arr)
    return answer
'''