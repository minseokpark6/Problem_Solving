def solution(numbers, hand):
    # 변수 지정
    answer = ''
    left, right = 77, 99
    
    # 키패트 위치 지정 
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [77, 0, 99]]
    
    # 누른 손가락 문자열 구하기
    for num in numbers:
        # 번호가 1, 4, 7인 경우
        if num in [1, 4, 7]:
            answer += "L"
            left = num
    
        # 번호가 3, 6, 9인 경우
        elif num in [3, 6, 9]:
            answer += "R"
            right = num
    
        # 번호가 2, 5, 8, 0인 경우
        else:
            # 현재 좌표값 구하기
            l_loca = [(i, j) for i in range(len(keypad)) for j in range(len(keypad[i])) if keypad[i][j]==left]
            r_loca = [(i, j) for i in range(len(keypad)) for j in range(len(keypad[i])) if keypad[i][j]==right]
            num_loca = [(i, j) for i in range(len(keypad)) for j in range(len(keypad[i])) if keypad[i][j]==num]

            # 엄지손가락의 위치와 num의 거리 구하기
            l_diff = abs(l_loca[0][0] - num_loca[0][0]) + abs(l_loca[0][1] - num_loca[0][1])
            r_diff = abs(r_loca[0][0] - num_loca[0][0]) + abs(r_loca[0][1] - num_loca[0][1])
            
            # 거리에 따른 손가락 구하기
            if l_diff > r_diff:
                answer += "R"
                right = num
            elif l_diff < r_diff:
                answer += "L"
                left = num
            else:
                if hand == "left":
                    answer += "L"
                    left = num
                else:
                    answer += "R"
                    right = num
    # 출력               
    return answer