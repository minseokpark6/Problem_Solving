def solution(food):
    # 변수 지정
    temp = ''
    
    # (1) 왼쪽에서부터 오른쪽으로 음식 배치하기 
    for i in range(1, len(food)):
        count = food[i]//2
        temp += (str(i)*count)
    
    # 물 + 오른쪽에서 왼쪽으로 음식 배치하기 
    answer = temp + "0" + temp[::-1]
        
    # 출력    
    return answer