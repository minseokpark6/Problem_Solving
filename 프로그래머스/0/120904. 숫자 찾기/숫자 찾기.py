def solution(num, k):
    str_num = str(num)
    if str(k) in str_num:
        idx = str_num.find(str(k)) + 1
        return idx
    else : 
        return -1
