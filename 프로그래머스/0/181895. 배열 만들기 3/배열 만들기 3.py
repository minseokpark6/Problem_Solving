def solution(arr, intervals):
    return arr[intervals[0][0]:intervals[0][1]+1] + arr[intervals[1][0]:intervals[1][1]+1]


'''
def solution(arr, intervals):
    answer = []
    for i in intervals:
        s, e = i[0], i[1]
        result = arr[s:e+1]
        for n in result:
            answer.append(n)
    return answer
'''