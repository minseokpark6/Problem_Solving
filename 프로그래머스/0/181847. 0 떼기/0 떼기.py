def solution(n_str):
    # 0으로 시작하지 않는 인덱스 찾기 
    for i, n in enumerate(n_str):
        if n != "0":
            idx = i
            break
    # 출력
    return n_str[idx:]


'''
def solution(n_str):
    result = [i for i in n_str]
    while result[0] == "0":
        del result[0]
    answer = "".join(result)
    return answer
'''