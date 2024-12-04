def solution(players, callings):
    # 딕셔너리에 players name하고, idx 저장
    dic = {n:idx for idx, n in enumerate(players)}
    
    # 순서 바꾸기
    for name in callings:
        win = dic[name]
        lose = dic[name] - 1

        # 딕셔너리에서 순위 변경
        dic[name], dic[players[lose]] = lose, win

        # 리스트에서 순위 변경
        players[lose], players[win] = players[win], players[lose]

    
    # 출력
    return players


"""
list의 index()는 시간 복잡도가 O(n)
for loop과 index()를 함께 사용하면 시간 복잡도는 O(n^2)으로 증가

dictionary는 hashing된 key에 따른 value를 찾는 과정이라 시간 복잡도가 O(1)
"""

"""
# 시간 초과

def solution(players, callings):
    # 순서 바꾸기
    for name in callings:
        idx = players.index(name)
        players[idx-1], players[idx] = players[idx], players[idx-1]
    
    # 출력
    return players
"""