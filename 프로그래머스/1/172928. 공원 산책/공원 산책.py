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