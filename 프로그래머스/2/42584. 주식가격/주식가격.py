def solution(prices):
    # 빈 리스트 생성
    answer = []
    
    # 가격이 떨어지지 않은 기간
    for idx in range(len(prices)):
        p, temp = prices[idx], 0

        while idx+1 < len(prices):
            idx += 1
            if p <= prices[idx]:
                temp += 1
            elif p > prices[idx]:
                temp += 1
                break
    
        answer.append(temp)
    
    # 출력
    return answer