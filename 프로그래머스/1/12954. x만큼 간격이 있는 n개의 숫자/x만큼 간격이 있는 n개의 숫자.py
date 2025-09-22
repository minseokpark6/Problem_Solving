def solution(x, n):
    return [i for i in range(x, (x*n)+x, x)] if x != 0 else [0]*n


'''
이전 코드 
- 양수 및 음수에 대한 별도 처리 불필요

def solution(x, n):
    if x > 0:
        return [i for i in range(x, (x*n)+1, x)]
    elif x < 0: 
        return [i for i in range(x, (x*n)-1, x)]
    else:
        return [0]*n
'''