def solution(left, right):
    # 약수의 개수 담을 리스트 생성 
    div = []
    # left - right까지의 모든 수 리스트 
    number = [i for i in range(left, right+1)]
    
    # 약수의 개수 카운트 
    for num in number:
        count = 0
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                if i**2 != num:
                    count += 2
                elif i**2 == num:
                    count +=1
        div.append(count)

    # 약수가 짝수일 경우 
    for idx, n in enumerate(div):
        if n % 2 != 0:
            number[idx] = -(number[idx])
    
    # 출력        
    return sum(number)