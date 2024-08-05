def solution(a, d, included):
    answer = 0
    result = []
    # 길이가 n인 등차수열 result 생성
    for i in range(len(included)):
        result.append(a)
        a += d
    # included의 값이 true인 인덱스 값과 result의 index값 비교
    for i in range(len(included)):
        if included[i] == True:
            answer += result[i]
    # 출력
    return answer