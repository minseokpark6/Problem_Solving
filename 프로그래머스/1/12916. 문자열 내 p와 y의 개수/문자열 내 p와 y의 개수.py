def solution(s):
    p_count = s.lower().count('p')
    y_count = s.lower().count('y')
    
    if p_count == y_count:
        return True
    elif p_count == 0 and y_count ==0:
        return True
    else:
        return False
    
 