def solution(keyinput, board):
    # 좌표 시작점 및 맵 크기 정의 
    x, y = 0, 0
    x_max, y_max = board[0]//2, board[1]//2

    # 좌표 이동
    for key in keyinput:
        if (key == 'left') and (x != -(x_max)):
            x -= 1
        elif (key == 'right') and (x != x_max):
            x += 1
        elif (key == 'up') and (y != y_max):
            y += 1
        elif (key == 'down') and (y != -(y_max)):
            y -= 1

    # 출력
    return [x, y]


'''
def solution(keyinput, board):
    answer = [0, 0]
    for i in keyinput:
        x_max = board[0] // 2
        y_max = board[1] // 2
        if i == 'up':
            if answer[1] == y_max:
                pass
            else:
                answer[1] += 1
        elif i == 'down':
            if answer[1] == -(y_max):
                pass
            else:
                answer[1] -= 1
        elif i == 'left':
            if answer[0] == -(x_max):
                pass
            else:
                answer[0] -= 1
        else:
            if answer[0] == x_max:
                pass
            else:
                answer[0] += 1
        
    return answer
'''