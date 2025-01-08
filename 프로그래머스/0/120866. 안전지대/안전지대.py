def solution(board):
    # board와 같은 구조의 map 정의
    bomb_map = [[1]*len(board[0]) for _ in range(len(board))]
    # 위험 지역 좌표 설정
    danger = [[0,0], [-1,0], [1,0], [0,1], [0,-1], [1,1], [-1,1], [1,-1], [-1,-1]]
    # 빈 리스트 정의 
    bomb_idx = []
    result = []
    
    # board에서 폭탄이 있는 좌표 구하기 
    for i_idx, i in enumerate(board):
        for j_idx, j in enumerate(i):
            if j == 1:
                bomb_idx.append([i_idx, j_idx])
    
    # bomb 좌표 + 위험 구역 좌표 >> 0으로 변경 
    for bomb in bomb_idx:
        for d in danger:
            # 지도 밖으로 나가지 않는 경우로 조건 제한 
            if 0 <= (bomb[0]+d[0]) < len(bomb_map) and 0 <= (bomb[1]+d[1]) < len(bomb_map[0]):
                bomb_map[bomb[0]+d[0]][bomb[1]+d[1]] = 0
    
    # 리스트에 추가 
    for b in bomb_map:
        result.extend(b)
    
    # 안전 구역(=1)의 값의 합 출력
    return sum(result)