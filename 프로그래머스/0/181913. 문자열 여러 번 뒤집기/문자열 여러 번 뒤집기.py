def solution(my_string, queries):
    # 문자열 뒤집기
    for q in queries:
        s, e = q[0], q[1]
        my_string = my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]
    # 출력
    return my_string


