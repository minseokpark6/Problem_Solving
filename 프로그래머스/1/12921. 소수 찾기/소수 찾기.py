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




# 이중 for문으로 인해, n의 개수가 커질 때, 시간이 너무 오래걸려서 통과 X

'''
def solution(n):
    answer = 0
    num_list = [i for i in range(2, n+1)]
    
    for num in num_list:
        sub = []
        for i in range(1, num+1):
            if num % i == 0:
                sub.append(i)
        if len(sub) == 2:
            answer += 1
    
    return answer
'''