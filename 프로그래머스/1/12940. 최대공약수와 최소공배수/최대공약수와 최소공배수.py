def solution(n, m):
    # 유클리드 호제법으로 최대공약수 구하기 
    a, b = n, m
    while b:
        a, b = b, a%b
    gcd = a
    
    # 최소공배수 = (n * m) // gcd
    lcm = (n * m) // gcd
    
    # 출력
    return [gcd, lcm]


'''
for 문으로 하나씩 비교해가면서 최대공약수를 찾는 방식보다 >> O(min(n, m))
유클리드 호제법으로 최대공약수를 구하는 것이 시간복잡도를 줄일 수 있음 >> O(log(min(n, m)))


## 기존 코드
def solution(n, m):
    # 변수 설정 -> 최대공약수 디폴트 값 
    gcd = 1
    # 최대공약수 구하기
    for i in range(min(n,m), 0, -1):
        if n%i == 0 and m%i==0:
            gcd = i
            break
    # 출력 
    return [gcd, (n*m)/gcd]
'''