def solution(my_string, queries):
    for q in queries:
        s, e = q[0], q[1]
        my_string = my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]
    return my_string