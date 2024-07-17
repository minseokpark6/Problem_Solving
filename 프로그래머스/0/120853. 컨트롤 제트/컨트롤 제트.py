def solution(s):
    answer = 0
    # 공백을 기준으로 문자열 분리 후 리스트에 저장
    temp = s.split(" ")
    # 'Z'값 변환 후 숫자로 타입 변경한 데이터를 담을 빈 리스트 생성
    nums = []
    # 'Z'값 변환 및 숫자 타입으로 변경
    for idx, i in enumerate(temp):
        if i == 'Z':
            nums.append(-(int(temp[idx-1])))
        else:
            nums.append(int(i))   
    # 모든 데이터의 합
    for num in nums:
        answer += num
    return answer