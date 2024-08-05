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
# 두 숫자가 같고, 하나의 숫자가 다른 경우

elif a == b or a == c or b == c :
        answer = (a + b + c) + ((a**2) + (b**2) + (c **2))
        
>> 이렇게 표현할 경우 세 개의 숫자가 모두 같은 경우까지 포함됨
'''