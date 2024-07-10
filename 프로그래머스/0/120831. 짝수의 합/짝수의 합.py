def solution(n):
    arr1 = range(2, n+1, 2)
    sum = 0 
    for i in arr1: 
        sum += i
    return sum