def solution(cards1, cards2, goal):
    # 변수 지정 
    result = []
    l1, l2 = len(cards1), len(cards2)
    idx_1, idx_2 = 0, 0
    
    # 가능 여부 확인
    for word in goal:
        if idx_1 < l1 and word == cards1[idx_1]:
            result.append(word)
            idx_1 += 1
        elif idx_2 < l2 and word == cards2[idx_2]:
            result.append(word)
            idx_2 += 1
        else:
            return "No"

    # 츌력  
    return "Yes"