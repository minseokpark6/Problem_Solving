def solution(n, words):
    # 빈 리스트 생성
    answer, result = [], []

    # 끝말잇기 첫 단어 result 리스트로 옮기기
    result.append(words[0])
    words.pop(0)
    
    # 끝말잇기 조건에 부합할 경우 result 리스트로 단어 옮기기
    while True:
        if result[-1][-1] == words[0][0] and words[0] not in result:
            result.append(words[0])
            words.pop(0)
        elif result[-1][-1] != words[0][0] or words[0] in result:
            if (len(result)+1) % n == 0:
                p = n
            else:
                p = (len(result)+1) % n
            i = (len(result)//n) + 1
            break
        
        if len(words) == 0:
            p, i = 0, 0
            break
    
    # 출력
    answer.append(p)
    answer.append(i)
    return answer



"""
(1)
p번 사람 
(len(result)+1) % n

if (len(result)+1) % n == 0:
    p = n
else:
    p = (len(result)+1) % n

(2)
i번째 차례
i = (len(result)//n) + 1


"""