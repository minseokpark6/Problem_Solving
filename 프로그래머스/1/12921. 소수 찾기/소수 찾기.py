import math 

def solution(n):
    if n < 2:
        return 0
    
    # 리스트 기반의 에라토스테네스의 체
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False 
    
    # 소수가 아닌 수 거르기 
    for i in range(2, int(math.sqrt(n))+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False 
    
    return sum(is_prime)


'''
## 개선점 
(1) 리스트(Boolean 배열) 기반의 에라토스테네스의 체로 변경 
- 포인트는 소수가 아닌 수를 제거할 때 삭제(removal)이냐, 표시(marking)이냐의 차이 
- 이전 코드에서는 집합에서 제거할 때 매번 새로운 집합을 생성 및 차집합을 연산 

(2) 배수의 범위 설정 변경 
- i*2 부터 시작할 경우 불필요한 제거가 반복됨 
- i*i 부터 시작해도 작은 수는 이미 이전의 반복문에서 제거가 되었기 때문에 i*i가 성능 면에서 유리 



## 이전 통과 코드 

# 에라토스테네스의 체( Sieve of Eratosthenes ) 알고리즘 
# 2에서부터 시작해, 각 소수의 배수를 제거해나가는 알고리즘

def solution(n):
    # 리스트 대신 집합을 사용
    # 1) 중복 처리를 신경쓰지 않아도 되고
    # 2) 리스트는 원소를 삭제할 때 모든 요소를 순차적으로 탐색해야 하지만, 집합은 해시 테이블을 사용하여 특정 원소를 찾고 제거하는 데 상수 시간(O(1))이 소요 (**)
    prime_nums = set(range(2, n+1))
    
    # 소수 선별 후 prime_nums에서 제거
    for i in range(1, int(n**0.5)+1):
        if i in prime_nums:
            prime_nums -= set(range(i*2,n+1,i))
            
    # for문에서 range의 끝을 int(n**0.5)+1로 설정한 이유 >> 효율성 때문
    # 소수의 배수를 지울 때, 특정 수의 배수는 그 수의 제곱근까지만 검사하면 충분
    

    # 정답 출력
    answer = len(prime_nums)
    
    return answer 

'''