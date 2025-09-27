def solution(price, money, count):
    total = sum(price*i for i in range(1, count+1))
    return total - money if total > money else 0


'''
(1) 리스트 컴프리헨션 vs 제너레이터 표현식 
- 불필요한 리스트 메모리 사용 X 

(2) sum 연산을 굳이 반복할 필요 없음

### 1차 코드 

def solution(price, money, count):
    cost = [price*(i+1) for i in range(count)]
    return sum(cost) - money if sum(cost) > money else 0
'''