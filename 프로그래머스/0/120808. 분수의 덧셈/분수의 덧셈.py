def gcd(a, b):        
    i = min(a, b)     
    while True:
        if a % i == 0 and b % i ==0:
            return i
        i -= 1
        
def lcm(a, b):
    i = max(a, b)
    while True:
        if i % a == 0 and i % b == 0:
            return i
        i += 1

def solution(numer1, denom1, numer2, denom2):
    answer = []
    denom = lcm(denom1, denom2)
    if denom == denom2:
        n = denom2 // denom1
        denom1 = denom1 * n
        numer1 = numer1 * n
        numer = numer1 + numer2
    elif denom == denom1:
        n = denom1 // denom2
        denom2 = denom2 * n
        numer2 = numer2 * n
        numer = (numer1 + numer2)
    else:
        n1 = denom // denom1
        n2 = denom // denom2
        denom1 = denom1 * n1
        numer1 = numer1 * n1
        denom2 = denom2 * n2
        numer2 = numer2 * n2
        numer = (numer1 + numer2)
    least = gcd(numer, denom)
    if least == 1:
        answer.append(numer)
        answer.append(denom)
    else:
        numer = numer // least
        denom = denom // least
        answer.append(numer)
        answer.append(denom)
  
    return answer