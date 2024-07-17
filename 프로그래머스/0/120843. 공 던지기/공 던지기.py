def solution(numbers, k):
    # 원형을 가장한 리스트 생성
    if len(numbers) < 2*k:
        numbers = numbers * k
    # 2명씩 2차원 리스트로 묶기
    numbers = [numbers[num:num+2] for num in range(0, len(numbers), 2)]
    # k번째 공을 던진 친구 번호 출력
    answer = numbers[k-1][0]    
    return answer