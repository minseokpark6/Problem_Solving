def solution(park, routes):
    # 공원의 가로, 세로 길이 정의 
    w, h = len(park[0]), len(park)

    # 방향 정보 정의 
    move = {'E' : (0, 1), 
            'W' : (0, -1),
            'S' : (1, 0),
            'N' : (-1, 0)}
    
    # 출발 위치 설정
    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                x, y = i, j


    # 주어진 방향으로 이동 
    for route in routes:
        op, n = route.split()   # 주어진 명령의 방향 및 거리 정의
        dx, dy = move[op]   # 방향 값 숫자로 환산 
        nx, ny = x, y   # 현재 위치 설정 
        flag = True     # 장애물, 공원의 범위를 벗어나는 경우 확인을 위한 bool
        
        # 한 칸씩 이동하면서 다음 두 가지를 먼저 확인
        for _ in range(int(n)):
            nx += dx
            ny += dy
            # 공원의 범위를 벗어나는 경우
            if not ((0 <= nx < h) and 0 <= ny < w):
                flag = False 
                break
            # 가는 길에 장애물이 있는 경우
            if park[nx][ny] == "X":
                flag = False
                break
        
        # 이동 경로에 문제가 없다면 이동 
        if flag:
            x, y = nx, ny
    
    return [x, y]

'''
def solution(park, routes):
    # 공원의 가로, 세로 길이 정의 
    w, h = len(park[0]), len(park)

    # 출발 위치 설정
    result = []
    for idx, i in enumerate(park):
        if 'S' in i:
            result.append(idx)
            result.append(i.find('S'))
            break

    # 주어진 방향으로 이동 
    for route in routes:
        op, n = route[0], int(route[-1])

        if op == 'E':
            # 공원을 벗어나는지 확인
            if (result[1]+n+1)>w:
                continue
            # 장애물을 만나는지 확인 
            if 'X' in park[result[0]][result[1]:result[1]+n+1]:
                continue
            # 둘다 없는 경우 이동
            result[1] += n
            
        elif op == 'W':
            # 공원을 벗어나는지 확인
            if (result[1]-n)<0:
                continue
            # 장애물을 만나는지 확인 
            if 'X' in park[result[0]][result[1]-n:result[1]+1]:
                continue
            # 둘다 없는 경우 이동
            result[1] -= n
            
        elif op == 'S':
            # 공원을 벗어나는지 확인
            if (result[0]+n+1)>h:
                continue
            # 장애물을 만나는지 확인 
            temp = [p[result[1]] for p in park]
            if 'X' in temp[result[0]:result[0]+n+1]:
                continue
            # 둘다 없는 경우 이동
            result[0] += n
            
        else:
            # 공원을 벗어나는지 확인
            if (result[0]-n) < 0:
                continue
            # 장애물을 만나는지 확인 
            temp = [p[result[1]] for p in park]
            if 'X' in temp[result[0]-n:result[0]+1]:
                continue
            # 둘다 없는 경우 이동
            result[0] -= n

    return result
'''