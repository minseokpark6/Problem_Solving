def solution(n, arr1, arr2):
    # 배열 이진수 변환
    temp1 = [format(i, 'b') for i in arr1]
    temp2 = [format(i, 'b') for i in arr2]
    
    # 이진수 변환 후 자리수 n으로 설정
    ar1 = ['0'*(n-len(i)) + i if len(i) < n else i for i in temp1]
    ar2 = ['0'*(n-len(i)) + i if len(i) < n else i for i in temp2]

    # 빈 리스트 생성
    answer = []
    
    # 암호 해독
    for a, b in zip(ar1, ar2):
        temp = ""
        for i, j in zip(a, b):
            if i == '1' or j == '1':
                temp += "#"
            else:
                temp += " "
        answer.append(temp)
        
    # 출력
    return answer



"""
# 넘파이 호출 안됨

import numpy as np
def solution(n, arr1, arr2):
    # 배열 이진수로 변환
    ar1 = np.array([int(format(i, 'b')) for i in arr1])
    ar2 = np.array([int(format(i, 'b')) for i in arr2])
    
    # 두 배열의 합 >> 지도 겹치기
    arr = [str(i) for i in (ar1 + ar2)]
    
    # 비밀지도 암호 해독
    for i in arr:
        # 이진수의 자리수가 다를 경우 맞춰주기
        if len(i) < n:
            i = '0'*(n-len(i)) + i
        temp = ""
        for num in i:
            if num == '1' or num == '2':
                temp += "#"
            else:
                temp += " "
        answer.append(temp)
        
    # 출력
    return answer
"""