def solution(a, b):
    if a > b:
        result = [n for n in range(b, a+1)]
    elif a < b: 
        result = [n for n in range(a, b+1)]
    else:
        result = [a]
    answer = sum(result)
    return answer