def solution(slice, n):
    result = n//slice
    return result if n%slice == 0 else result+1
    
    
    
'''
def solution(slice, n):
    answer = n // slice
    if n % slice == 0:
        return answer 
    else:
        return answer + 1
'''