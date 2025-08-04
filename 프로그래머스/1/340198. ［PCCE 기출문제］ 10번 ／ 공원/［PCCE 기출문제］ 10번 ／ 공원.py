def solution(mats, park):
    # 공원의 넓이 정의
    W, H = len(park[0]), len(park)
    # 주어진 돗자리 중 가장 큰 돗자리부터 탐색
    mats.sort(reverse=True)

    # 특정 위치에 돗자리를 놓을 수 있는지 확인하는 함수 정의 
    def can_place(h, w, m):
        if h+m > H or w+m > W:
            return False 
        return all(park[i][j] == "-1" for i in range(h, h+m) for j in range(w, w+m))

    '''
    all 함수는 범위 안에 모든 조건이 참일 때만, True를 반환
    이 중 하나라도 조건에 해당하지 않으면 False를 반환 
    '''
    
    # 가장 큰 돗자리부터 확인 
    for mat in mats:
        for i in range(H-mat+1):
            for j in range(W-mat+1):
                if can_place(i, j, mat):
                    # 출력
                    return mat

    # 돗자리가 위치할 수 없는 경우 출력
    return -1