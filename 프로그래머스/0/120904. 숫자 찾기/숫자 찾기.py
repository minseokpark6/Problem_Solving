def solution(num, k):
    for idx, n in enumerate(str(num)):
        if str(k) == n:
            return idx + 1
    return -1

'''
def solution(num, k):
    str_num = str(num)
    if str(k) in str_num:
        idx = str_num.find(str(k)) + 1
        return idx
    else : 
        return -1
'''