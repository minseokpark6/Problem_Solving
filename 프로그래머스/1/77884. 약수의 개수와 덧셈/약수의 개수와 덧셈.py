def solution(left, right):
    # 변수 정의 
    total = 0
    # 제곱수 판별 
    for num in range(left, right+1):
        if int(num**0.5) ** 2 == num:
            total -= num 
        else:
            total += num 
    # 출력
    return total 

'''
(1) 모든 약수의 개수를 구할 필요가 없음 
-> 약수의 개수가 홀수인지 짝수인지만 판별하면 가능 
-> 약수의 개수가 홀수인 경우는 제곱수, 나머지는 모두 짝수 

(2) 불필요한 리스트 사용 X 
-> number, div 등의 리스트 사용 시 메모리 증가 

(3) enumerate를 사용하여 중첩 계산 풀필요 
'''

''' 이전 코드
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
'''