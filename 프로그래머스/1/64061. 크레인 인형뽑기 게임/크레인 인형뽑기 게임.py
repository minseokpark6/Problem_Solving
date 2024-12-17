def solution(board, moves):
    # 변수 지정
    answer = 0
    stack = []
    
    for num in moves:
        # num의 가장 위에 있는 인형을 뽑기
        idx = 0
        while True:
            if board[idx][num-1] != 0:
                # 뽑힌 인형 변수 지정
                selected = board[idx][num-1]
                # 바구니가 비어있는 경우 추가
                if not stack:
                    stack.append(selected)
                    board[idx][num-1] = 0
                    break
                # 바구니에 인형이 있는 경우 비교
                # 바구니 맨 위 인형과 뽑은 인형이 같을 경우
                if stack[-1] == selected:
                    stack.pop()
                    answer += 2
                    board[idx][num-1] = 0
                # 바구니 맨 위 인형과 뽑은 인형이 다른 경우
                else:
                    stack.append(selected)
                    board[idx][num-1] = 0
                break

            elif board[idx][num-1] == 0:
                idx += 1
                
            # 해당 칸에 인형이 없는 경우 
            if len(board) <= idx:
                break
        
    return answer