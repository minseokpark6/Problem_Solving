def solution(n_str):
    result = [i for i in n_str]
    while result[0] == "0":
        del result[0]
    answer = "".join(result)
    return answer
        