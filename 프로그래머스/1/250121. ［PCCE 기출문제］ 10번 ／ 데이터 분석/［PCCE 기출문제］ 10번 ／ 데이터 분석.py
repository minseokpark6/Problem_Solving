def solution(data, ext, val_ext, sort_by):
    # 변수 정의
    answer = []
    # 조건에 맞는 데이터 선별
    for d in data:
        if ext == 'code':
            if d[0] < val_ext:
                answer.append(d)
        elif ext == 'date':
            if d[1] < val_ext:
                answer.append(d)
        elif ext == 'maximum':
            if d[2] < val_ext:
                answer.append(d)
        else:
            if d[3] < val_ext:
                answer.append(d)
    # 데이터 정렬 
    if sort_by == 'code':
        answer.sort(key = lambda x:x[0])
            
    elif sort_by == 'date':
        answer.sort(key = lambda x:x[1])
         
    elif sort_by == 'maximum':
        answer.sort(key = lambda x:x[2])
            
    else:
        answer.sort(key = lambda x:x[3])
    # 출력     
    return answer