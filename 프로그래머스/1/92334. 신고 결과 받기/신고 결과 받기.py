def solution(id_list, report, k):
    # 신고 내역을 유저 아이디 별로 정리
    details = {id:[] for id in id_list}
    for i in report:
        user = i.split(' ')
        details[user[0]].append(user[1])

    # 중복 제거 (한 유저의 동일 유저 중복 처리)
    details = {k:list(set(v)) for k,v in details.items()}
    
    # 유저 별로 신고당한 횟수 카운트
    reported = {id:0 for id in id_list}
    for l in details.values():
        for user in l:
            reported[user] += 1
            
    # 정지된 id 리스트에 담기
    suspended = []
    for ke, va in reported.items():
        if va >= k:
            suspended.append(ke)
    
    # 처리 결과 메일을 받은 횟수 카운트
    received = {id:0 for id in id_list}
    for ke, va in details.items():
        for user in va:
            if user in suspended:
                received[ke] += 1

    # 처리 결과 메일을 받은 횟수만 리스트로 출력
    return [c for c in received.values()]