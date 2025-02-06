def solution(skill, skill_trees):
    # 변수 정의 
    cnt = 0   # 가능한 스킬트리 개수
    
    # skill_trees에 들어있는 스킬만 따로 저장
    answer = []
    for trees in skill_trees:
        temp = ""
        for t in trees:
            if t in skill:
                temp += t
        answer.append(temp)
    
    # skill과 answer에 들어있는 스킬트리 비교 
    for s in answer:
        if s == skill[:len(s)]:
            cnt += 1

    # 출력 
    return cnt