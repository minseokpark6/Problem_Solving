def solution(binomial):
    result = binomial.split(" ")
    a, b = int(result[0]), int(result[2])
    if result[1] == "+":
        answer = a + b
    elif result[1] == "-":
        answer = a - b
    else:
        answer = a*b
    return answer