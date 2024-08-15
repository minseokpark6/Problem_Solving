def solution(arr):
    answer = 0
    while True:
        # 별도의 빈 리스트 생성
        result = []
        
        # arr 원소 값 정리
        for n in arr:
            if (n >= 50) and (n % 2 == 0):
                n = n // 2
                result.append(n)
            elif (n < 50) and (n % 2 != 0):
                n = 2*n + 1
                result.append(n)
            else:
                result.append(n)
                
        # arr(x) = arr(x+1) 확인        
        if arr == result:
            break
        else:
            arr = result
            answer += 1
            
    return answer