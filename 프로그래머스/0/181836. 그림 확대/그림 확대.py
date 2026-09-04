def solution(picture, k):
    # 가로 k배 늘리기 
    arr = ["".join(k*s for s in p) for p in picture]
    # 세로 k배 늘려서 출력
    return [i for i in arr for _ in range(k)]
    

'''
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
'''