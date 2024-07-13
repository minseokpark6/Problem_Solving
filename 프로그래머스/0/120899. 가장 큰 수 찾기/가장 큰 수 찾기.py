def solution(array):
    max_num = array[0]
    answer = []
    
    for i in array:
        if max_num < i:
            max_num = i
            
    idx = array.index(max_num)
    
    answer.append(max_num)
    answer.append(idx)
    
    return answer