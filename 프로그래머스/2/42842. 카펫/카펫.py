def solution(brown, yellow):
    # 변수 정의
    total = brown + yellow 
    
    # 가로, 세로값 찾기 
    for height in range(3, int(total**0.5)+1):
        if total % height == 0:
            width = total // height 
            
            if (width-2) * (height-2) == yellow:
                return [width, height]


'''
(1) 탐색 범위 변경 
- total의 약수 기반 탐색 
- 불필요한 계산 제거 

(2) 불필요한 리스트
- 바로 출력 



## 기존 통과 코드 

def solution(brown, yellow):
    # 변수 정의
    result = []
    
    # 가로, 세로값 찾기 >> a(가로)의 길이는 brown 수의 반보다 작을 수 밖에 없음
    for i in range(3, brown//2):
        a, b = i, (brown+4)/2 - i
        if a*b == brown+yellow and (a>=b):
            result.append(a)
            result.append(b)
    
    # 출력 
    return result


## 코드 해설
return = [a, b] 라고 가정했을 때, 

(1) a, b는 brown과 yellow의 합의 약수로 이루어져 있음 
a * b = brown + yellow

(2) brown은 1줄로 이루어진 테두리이기 때문에 
(b-2)가 yellow의 세로줄 수 
(a-2)가 yellow의 가로줄 수 

(3) 
고로 brown의 개수는 
brown = (a-2)*2 + (b-2)*2 + 4 = 2*(a+b) - 4
a+b = (brown+4)/2
b = (brown+4)/2 -a

'''