def solution(arr):
    return [
        i//2 if i >=50 and i%2==0 
        else i*2 if i<50 and i%2==1
        else i 
        for i in arr
    ]

'''
def solution(arr):
    answer = []
    for i in arr:
        if i >= 50 and i % 2 == 0:
            i = i / 2
        elif i < 50 and i % 2 == 1 :
            i *= 2
        else: 
            pass
        answer.append(i)
    return answer
'''