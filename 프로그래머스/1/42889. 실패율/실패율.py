def solution(N, stages):
    # 변수 설정 
    dic = {}
    
    # stage 별 실패율 구하기
    all = len(stages)
    for i in range(1, N+1):
        if all != 0:
            user_count = stages.count(i)
            dic[i] = user_count/all
            all -= user_count
        else:
            dic[i] = 0
    
    # 출력
    return [k for k, v in sorted(dic.items(), key = lambda item: (-item[1], item[0]))]

"""
(1) (-item[1], item[0])
- item[1] : value 을 지칭 >> "-" 내림차순으로 정렬
- item[0] >> key값 >> 오름차순 정렬 
_ 튜플로 묶어서 순서대로 value 값으로 내림차순 후 key값으로 오름차순 정렬
"""