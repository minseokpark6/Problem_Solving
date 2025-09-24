def solution(absolutes, signs):
    # 변수 정의 
    result = 0
    # 정수의 합 구하기
    for idx, n in enumerate(absolutes):
        result += n if signs[idx] == True else (-n)
    # 출력
    return result

''' 이전 코드 
>> 리스트 사용 불필요
- 메모리 문제 

def solution(absolutes, signs):
    result = []
    for idx, n in enumerate(absolutes):
        if signs[idx] == True:
            result.append(n)
        else:
            result.append(-n)
    answer = sum(result)
    return answer
'''