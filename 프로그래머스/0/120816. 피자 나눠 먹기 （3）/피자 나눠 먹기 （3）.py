def solution(slice, n):
    answer = n // slice
    if n % slice == 0:
        return answer 
    else:
        return answer + 1