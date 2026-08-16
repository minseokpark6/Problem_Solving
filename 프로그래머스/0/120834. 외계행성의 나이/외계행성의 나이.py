def solution(age):
    # 변수 정의 
    alpha = "abcdefghij"
    
    # 나이 변환 출력
    return "".join(alpha[int(a)] for a in str(age))
        


'''
def solution(age):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    answer = []
    for i in list(str(age)):
        answer.append(alpha[int(i)])
    answer = ''.join(answer)
    return answer
'''
