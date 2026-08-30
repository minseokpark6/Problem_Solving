def solution(my_string):
    # 변수 정의
    result = [0] * 52
    
    # 각 문자의 개수 찾기
    for s in my_string:
        if s.isupper():
            result[ord(s) - ord('A')] += 1
        else:
            result[ord(s) - ord('a') + 26] += 1

    # 출력
    return result

'''
def solution(my_string):
    al = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    answer = [0] * len(al)
    for idx, a in enumerate(al):
        if a in my_string:
            answer[idx] += my_string.count(a)
    return answer
'''