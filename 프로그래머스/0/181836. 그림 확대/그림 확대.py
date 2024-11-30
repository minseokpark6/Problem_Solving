def solution(picture, k):
    # 빈 리스트 생성
    answer = []
    # 그림 확대하기
    for i in picture: 
        temp = ""
        for j in i:
            j *= k
            temp += j
        
        for _ in range(k):
            answer.append(temp)
    # 출력
    return answer