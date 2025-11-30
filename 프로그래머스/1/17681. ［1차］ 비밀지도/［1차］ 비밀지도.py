def solution(n, arr1, arr2):
    # 출력
    return [format(a|b, 'b').zfill(n).replace('1', '#').replace('0', ' ') for a, b in zip(arr1, arr2)]

'''

## 리스트 컴프리헨션 이전 가독성 버전 코드 

def solution(n, arr1, arr2):
    # 변수 정의 
    result = []
    
    # 암호 해독
    for a, b in zip(arr1, arr2):
        row = format(a|b, 'b').zfill(n) # 비트 or 연산 후 이진수 자리수 채우기
        row = row.replace('1', '#').replace('0', ' ')
        result.append(row)
    
    # 출력
    return result
    

(1) 비트 연산 + zfill을 활용해 이진수 + 이진수 자리수 해결 
(2) replace 활용


## 이전 통과 코드 
def solution(n, arr1, arr2):
    # 배열 이진수 변환 
    m1 = [format(i, 'b') for i in arr1]
    m2 = [format(i, 'b') for i in arr2]
    
    # 이진수 자리수 맞추기 
    map1 = ['0'*(n-len(i))+i if len(i)<n else i for i in m1]
    map2 = ['0'*(n-len(i))+i if len(i)<n else i for i in m2]
    
    # 암호 해독
    answer = []
    for a, b in zip(map1, map2):
        temp = []
        for i, j in zip(a, b):
            if i == '1' or j == '1':
                temp.append("#")
            else:
                temp.append(" ")
        answer.append("".join(temp))
    
    # 출력
    return answer  
    
    '''