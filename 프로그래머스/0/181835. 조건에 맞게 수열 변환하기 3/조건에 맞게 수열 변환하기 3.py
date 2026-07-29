def solution(arr, k):
    return [i*k if k%2!=0 else i+k for i in arr]

'''
def solution(arr, k):
    answer = []
    for n in arr:
        if k % 2 != 0:
            answer.append(n * k)
        else:
            answer.append(n + k)
    return answer
'''