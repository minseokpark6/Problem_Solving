def solution(keymap, targets):
    # 최단 key touch 설정
    dic = {}
    for key in keymap:
        for idx, i in enumerate(key):
            if i not in dic:
                dic[i] = idx+1
            elif dic[i] > idx+1:
                dic[i] = idx+1
    
    # 최단 touch 구하기 
    answer = []
    for target in targets:
        touch = 0
        for t in target:
            if t in dic:
                touch += dic[t]
            else:
                touch = -1
                break
        answer.append(touch)

    # 출력           
    return answer