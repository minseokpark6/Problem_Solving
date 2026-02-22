def solution(n):
    # 나머지가 1이 되는 가장 작은 수 찾기
    return next(i for i in range(2, n) if n%i==1)

'''
## next 
- 조건을 만족하는 첫 번째 값 반환


## 이전 코드
def solution(n):
    # 변수 설정
    num = 2
    # 나머지가 1이 되는 가장 작은 수 찾기
    while True:
        if n%num == 1:
            answer = num
            break
        num +=1

    # 출력
    return answer
'''
        