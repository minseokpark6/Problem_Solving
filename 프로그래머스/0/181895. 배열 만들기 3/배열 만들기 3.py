def solution(arr, intervals):
    answer = []
    for i in intervals:
        s, e = i[0], i[1]
        result = arr[s:e+1]
        for n in result:
            answer.append(n)
    return answer