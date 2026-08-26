def solution(my_string):
    # 문자열 제거 
    for s in my_string:
        if s.isalpha():
            my_string = my_string.replace(s, " ")
    
    # 숫자의 합 출력
    return sum(int(n) for n in my_string.split(" ") if n)

'''
def solution(my_string):
    answer = 0
    num = 0
    for i in my_string:
        if i.isdigit():
            num = num*10 + int(i)    
        else :
            answer += num
            num = 0
    answer += num
    return answer
'''