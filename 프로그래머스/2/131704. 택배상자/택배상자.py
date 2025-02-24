def solution(order):
    # 변수 정의
    cnt = 0     # 트럭에 실은 상자의 개수 카운트 
    stack = []  # 보조 컨테이너 
    num = 1     # 택배 기사님이 원하는 상자를 놓는 순서
    idx = 0     
    
    # 컨테이너의 짐 싣기 
    while idx < len(order):
        if order[idx] == num:
            num += 1
            cnt += 1
            idx += 1
            
        elif len(stack) > 0 and order[idx] == stack[-1]:
            stack.pop()
            cnt += 1
            idx += 1
            
        else:
            if num <= len(order):
                stack.append(num)
                num += 1
            else:
                break
    
    # 출력
    return cnt