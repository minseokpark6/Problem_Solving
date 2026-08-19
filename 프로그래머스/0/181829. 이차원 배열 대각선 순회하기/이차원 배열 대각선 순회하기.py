def solution(board, k):
    # 출력 
    return sum(
    board[i][j] for i in range(min(len(board), k+1))
        for j in range(min(len(board[i]), k-i+1))
        if i + j <= k
    )



'''
def solution(board, k):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i + j <= k:
                answer += board[i][j]
    return answer
'''