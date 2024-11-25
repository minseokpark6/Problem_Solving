def solution(elements):
    # 변수 지정
    temp = elements*2
    result = []
    
    # 연속 부분 수열 합으로 만들 수 있는 수의 개수 구하기
    for d in range(len(elements)):
        for idx in range(len(elements)):
            result.append(sum(temp[idx:idx+d+1]))
    
    # 출력
    return len(list(set(result))) 


"""
길이가 1
[7,9,1,1,4]
7
9
1
1
4

길이가 2 
7, 9 = 16
9, 1 = 10
1, 1 = 2
1, 4 = 5
4, 7 = 11

길이가 3 
7,9,1 
9,1,1
1,1,4
1,4,7
4,7,9
"""