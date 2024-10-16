def solution(n, m):
    gcd = 1
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            gcd = i 
            break
    answer = [gcd, (n*m)/gcd]
    return answer

