def solution(myString, pat):
    # 빈 문자열 생성
    answer = ''
    # 문자열 인덱스 찾기 (find: 왼쪽부터 인덱스, rfind: 오른쪽부터 인덱스)
    a = myString.rfind(pat)
    
    # pat의 길이가 1인 경우
    if len(pat) == 1 :
        for i in range(len(myString)) :
            if a + 1 > i :
                answer = answer + myString[i]

    # pat의 길이가 1이 아닌 경우
    else :
        for j in range(len(myString)) : 
            if a > j : 
                answer = answer + myString[j]
        answer = answer + myString[a:a+len(pat)]

    return answer