def solution(str1, str2):
    result = []
    for i in range(len(str1)):
        a = str1[i]
        result.append(a)
        b = str2[i]
        result.append(b)
    answer = ''.join(result)
    return answer