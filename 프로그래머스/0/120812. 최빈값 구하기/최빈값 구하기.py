def solution(array):
    answer = 0
    arr1 = [0] * 1001
    
    for idx in array:
        arr1[idx] += 1
    
    maxf = max(arr1)
    
    if arr1.count(maxf) > 1:
        return -1
    else:
        answer = arr1.index(maxf)
        return answer 