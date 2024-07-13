def solution(cipher, code):
    l = len(cipher)
    answer = ''
    
    # answer 추출
    for idx in range(code-1, l, code):
        answer += cipher[idx]
    return answer