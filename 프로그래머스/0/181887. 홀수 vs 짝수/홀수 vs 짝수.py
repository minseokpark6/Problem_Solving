def solution(num_list):
    even = 0
    odd = 0
    # 홀수 번째 원소들의 합 & 짝수 번째 원소들의 합 구하기
    for idx, num in enumerate(num_list):
        if idx % 2 == 0:
            odd += num
        else :
            even += num
    # 둘 중 큰 것을 출력
    if even >= odd:
        return even
    else:
        return odd