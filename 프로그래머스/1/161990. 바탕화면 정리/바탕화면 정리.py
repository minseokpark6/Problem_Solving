def solution(wallpaper):
    # 변수 설정 
    answer = []
    
    # 파일 위치 확인 후 점 S와 점 E 좌표 설정 
    for i, arr in enumerate(wallpaper):
        for j, file in enumerate(arr):
            if file == "#":
                if not answer:
                    lux, luy, rdx, rdy = i, j, i+1, j+1
                    answer.extend([lux,luy,rdx,rdy])
                else:
                    if answer[0] > i :
                        answer[0] = i
                    if answer[1] > j :
                        answer[1] = j
                    if answer[2] < i+1:
                        answer[2] = i+1
                    if answer[3] < j+1:
                        answer[3] = j+1      
    # 출력
    return answer