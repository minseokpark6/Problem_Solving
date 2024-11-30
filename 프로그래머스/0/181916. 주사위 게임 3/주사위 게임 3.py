def solution(a, b, c, d):
    # 변수 지정
    temp = [a, b, c, d]
    dic = {num:temp.count(num) for num in set(temp)}
    sorted_dic = dict(sorted(dic.items(), key= lambda item: item[1], reverse=True))
    
    # 네 주사위의 숫자를 통한 점수 구하기
    if len(dic) == 1:
        answer = 1111 * list(dic.keys())[0]
    elif len(dic) == 2:
        p, q = list(sorted_dic.keys())[0], list(sorted_dic.keys())[1]
        if 2 in sorted_dic.values():
            answer = (p+q) * abs(p-q)
        elif 3 in sorted_dic.values():
            answer = (10*p + q) ** 2
            
    elif len(dic) == 3:
        q, r = list(sorted_dic.keys())[1], list(sorted_dic.keys())[2]
        answer = q * r
    else:
        answer = min(list(sorted_dic.keys()))
        
    # 출력
    return answer