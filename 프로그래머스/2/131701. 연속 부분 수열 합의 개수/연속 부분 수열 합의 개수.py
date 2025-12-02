## 누적합 활용 버전 코드 

def solution(elements):
    # 변수 정의 
    n = len(elements)
    arr = elements * 2
    result = set()
    
    # 1. 누적합 리스트 정의
    prefix = [0] * (2 * n + 1)
    for i in range(1, 2*n + 1):
        prefix[i] = prefix[i-1] + arr[i-1]
        
    # 2. 연속 부분 수열의 합 정의 
    for length in range(1, n+1):
        for start in range(n):
            result.add(prefix[start+length] - prefix[start])
    
    # 3. 합의 개수 출력
    return len(result)

        

'''

## 슬라이싱 윈도우 활용 ver.

def solution(elements):
    # 변수 정의 
    n = len(elements)
    arr = elements * 2
    result = set()

    # 연속 부분 수열 합의 개수 구하기 
    for length in range(1, n+1):
        # 처음 부분합 미리 계산 
        current_sum = sum(arr[:length])
        result.add(current_sum)
        
        # 슬라이딩 윈도우로 다음 부분합 계산
        for i in range(1, n):
            current_sum += arr[i+ length - 1] - arr[i - 1]
            result.add(current_sum)
    
    # 출력
    return len(result)


## 개선 부분 

(1) 기존 통과 코드 => O(n³)
- for 문 => O(n)
- 2차 for문 => O(n)
- sum() 함수 내 슬라이싱할 때 평균 = > O(n)

=> 이중 for문 + 슬라이싱 윈도우 or 누적합의 방식으로 개선 => O(n²)

(2) 슬라이싱 윈도우 

# 예시 

elements = [7, 9, 1]
arr = elements * 2 = [7, 9, 1, 7, 9, 1]

이전 구간: arr[0:3] → [7, 9, 1]
다음 구간: arr[1:4] → [9, 1, 7]

=> arr[0]의 값을 제외하고, arr[3]의 값을 집어 넣는 방식


## 이전 통과 코드 

def solution(elements):
    # 변수 정의 
    temp = elements*2
    result = []

    # 연속 부분 수열 합의 개수 구하기 
    for distance in range(len(elements)):
        for idx in range(len(elements)):
            result.append(sum(temp[idx:idx+distance+1]))

    # 출력
    return len(set(result))
    '''