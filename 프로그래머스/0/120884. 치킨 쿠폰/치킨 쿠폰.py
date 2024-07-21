def solution(chicken):
    # 서비스로 받을 수 있는 치킨 수
    extra_chicken = chicken // 10
    answer = extra_chicken
    
    # 서비스로 치킨을 받고 남은 쿠폰 수 
    coupon = chicken % 10
    
    # 서비스로 받은 치킨을 통해 받는 쿠폰 및 추가 서비스 치킨 수
    while True:
        if extra_chicken >= 10:
            coupon += extra_chicken
            extra_chicken = coupon // 10
            answer += extra_chicken
            coupon = coupon % 10
        else:
            coupon += extra_chicken
            break

    # 남은 쿠폰으로 추가로 받을 수 있는 치킨 수
    if coupon >= 10:
        answer += coupon // 10
            
    return answer

'''
입력값 〉 1999
기댓값 〉 222

199 + 20 + 2 + 1

9 + 199 = 208

8 + 20 = 28

8 + 2 = 10

'''