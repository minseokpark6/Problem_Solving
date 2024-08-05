def solution(num_list):
    sum = 0
    mul = 1
    # num_list 내의 숫자의 합과 곱 구하기
    for num in num_list:
        sum += num
        mul *= num
    
    # 숫자의 합의 제곱
    sum = sum ** 2
    
    # 크기 비교 후 출력 
    if sum > mul:
        return 1
    elif sum < mul :
        return 0