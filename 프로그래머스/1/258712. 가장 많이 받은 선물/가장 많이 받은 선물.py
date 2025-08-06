from itertools import combinations

def solution(friends, gifts):
    # 다음 달에 받을 선물 횟수 딕셔너리 정의
    next = {f:0 for f in friends} 
    # 선물 지수 딕셔너리 정의
    gift_dic = {f:0 for f in friends} 
    # 주고 받은 선물 카운트 딕셔너리 정의
    gift_matrix = {
        giver: {receiver: 0 for receiver in friends if receiver != giver} 
        for giver in friends
        } 

    # 선물 지수 및 주고 받은 선물 횟수 카운트
    for gift in gifts:
        giver, receiver = map(str, gift.split())
        # 선물 지수 정리
        gift_dic[giver] += 1
        gift_dic[receiver] -= 1
        # 주고 받은 선물 카운트 
        gift_matrix[giver][receiver] += 1

    # 다음 달에 받을 선물 개수 카운트
    for i in combinations(friends, 2):
        a, b = i[0], i[1]
        # 선물을 주고 받은 적이 있는 경우 
        if gift_matrix[a][b] != 0 or gift_matrix[b][a] != 0:
            if gift_matrix[a][b] > gift_matrix[b][a]:
                next[a] += 1
            elif gift_matrix[a][b] < gift_matrix[b][a]:
                next[b] += 1
            # 주고 받은 횟수가 같은 경우
            else:
                if gift_dic[a] > gift_dic[b]:
                    next[a] += 1
                elif gift_dic[a] < gift_dic[b]:
                    next[b] += 1
            
        # 선물을 주고 받은 적이 없는 경우
        else:
            if gift_dic[a] > gift_dic[b]:
                next[a] += 1
            elif gift_dic[a] < gift_dic[b]:
                next[b] += 1
    # 출력
    return max(next.values())