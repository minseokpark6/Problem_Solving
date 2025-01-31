def solution(land):
    # 마지막 행까지 내려왔을 때 최대값 구하기
    for i in range(1, len(land)):   # 전 행의 최대값과의 합을 위해 1행부터 시작
        for j in range(4):          # 열은 모두 4개
            # 열이 일치하지 않는 k 중의 최대값을 하나씩 더해서 내려가기
            land[i][j] += max(land[i-1][k] for k in range(4) if k != j)
    # 마지막 행의 최대값 출력
    return max(land[-1])