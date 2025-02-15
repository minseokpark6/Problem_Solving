def solution(board, h, w):
    # (1), (2) 변수 정의
    n, cnt = len(board), 0
    
    # (3) h와 w의 변화량 리스트 정의 
    dh, dw = [0, 1, -1, 0], [1, 0, 0, -1]
    
    # (4) 같은 색 카운트
    for i in range(4):
        h_check, w_check = h + dh[i], w + dw[i]
        if h_check >= 0 and h_check < n and w_check >= 0 and w_check < n:
            if board[h][w] == board[h_check][w_check]:
                cnt += 1
    # (5) 출력            
    return cnt