def solution(n):
    return sum(i for i in range(n+1) if i%2==0)


'''
def solution(n):
    arr1 = range(2, n+1, 2)
    sum = 0 
    for i in arr1: 
        sum += i
    return sum

'''