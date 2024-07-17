def solution(n):
    answer =  []
    d = 2

    while n > 1:
        if n % d == 0:
            answer.append(d)
            n //= d
        else:
            d += 1
    
    return sorted(list(set(answer)))