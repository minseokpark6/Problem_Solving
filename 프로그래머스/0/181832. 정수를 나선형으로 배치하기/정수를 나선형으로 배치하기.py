def solution(n):
    # 0으로 채운 2차원 리스트 생성
    answer = [[0 for _ in range(n)] for _ in range(n)]
    # 방향키 설정
    direction = [[1,0], [0,1], [-1, 0], [0, -1]]*n
    dir_idx = -1
    # 방향키 횟수 설정 
    times = [n-1] + [i for i in range(n-1,0,-1) for _ in range(2)]
    # 좌표 설정
    x, y = 0, 0
    # 삽입할 숫자 변수 설정
    num = 1
    # 리스트 시작점 숫자 채우기 
    answer[y][x] = num
    
    # 나머지 리스트 채우기
    for time in times:
        dir_idx += 1
        for _ in range(time):
            num+=1
            x += direction[dir_idx][0]
            y += direction[dir_idx][1]
            answer[y][x] = num
    

    # 출력
    return answer


"""
n = 4
3/ 3/3/2/2/1/1

n = 5
4/ 4/4/3/3/2/2/1/1/

n = 6
5/ 5/5/4/4/3/3/2/2/1/1

n = 7
6/ 6/6/5/5/4/4/3/3/2/2/1/1
"""