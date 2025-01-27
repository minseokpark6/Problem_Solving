def solution(numbers):
    # 리스트 생성
    answer = [-1] * len(numbers)
    stack = []    # 인덱스 저장용
    
    # 뒷 큰 수 찾기
    for idx, num in enumerate(numbers):
        # 저장되어 있는 인덱스를 돌면서 뒤에 더 큰 수가 나올 경우, stack에서 인덱스를 제거하며 answer에 저장
        while stack and numbers[stack[-1]] < num:
            answer[stack.pop()] = num
    
        # 다음 반복문에서의 크기 비교를 위해 stack에 인덱스 추가
        stack.append(idx)


    # 출력
    return answer

"""
# 시간 초과 >> 불통
>> 이중 for문이 가장 큰 문제

def solution(numbers):
    # 빈 리스트 생성
    answer = []
    
    # 뒷 큰 수 찾기
    for idx, num in enumerate(numbers):

        # num의 뒤에 있는 숫자 리스트 정의
        temp = numbers[idx+1:]

        # 뒤에 숫자가 있는 경우
        if (idx+1) < len(numbers):
            for i, num_ in enumerate(temp):
                if i+1 == len(temp):
                        if num < num_:
                            answer.append(num_)
                        else:
                            answer.append(-1)
                else:
                    if num < num_:
                        answer.append(num_)
                        break

        # 리스트 내 마지막 숫자인 경우
        elif (idx+1) >= len(numbers):
            answer.append(-1)

    # 출력
    return answer

"""