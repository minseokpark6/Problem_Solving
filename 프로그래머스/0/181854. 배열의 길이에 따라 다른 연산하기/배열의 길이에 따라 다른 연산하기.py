def solution(arr, n):
    # 변수 정의
    start = len(arr)%2
    # 출력
    return [num+n if idx%2!=start else num for idx, num in enumerate(arr)]


           

'''
def solution(arr, n):
    answer = []
    for idx, num in enumerate(arr):
        if len(arr) % 2 != 0:
            if idx % 2 == 0:
                num += n
            answer.append(num)
        else:
            if idx % 2 != 0:
                num += n
            answer.append(num)      
    return answer
'''