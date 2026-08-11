def solution(a, b, c):
    total = a + b + c

    if a == b == c:
        return total * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)

    elif a == b or b == c or a == c:
        return total * (a**2 + b**2 + c**2)

    else:
        return total
         
        
'''
def solution(a, b, c):
    # 세 숫자가 모두 같은 경우
    if a == b and b == c:
        answer = (3 * a) * (3 * (a**2)) * (3 * (a**3))
        
    # 두 숫자가 같고, 하나의 숫자가 다른 경우
    elif a == b and a != c:
        answer = (a + b + c) * ((a**2) + (b**2) + (c **2))
    elif a == c and a != b:
        answer = (a + b + c) * ((a**2) + (b**2) + (c **2))
    elif b == c and a != b:
        answer = (a + b + c) * ((a**2) + (b**2) + (c **2))
    
    # 세 숫자가 모두 다른 경우
    else :
        answer = a + b + c
    
    return answer
'''