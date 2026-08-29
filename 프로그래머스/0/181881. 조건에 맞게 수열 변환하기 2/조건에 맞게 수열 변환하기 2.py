def solution(arr):
    # 변수 정의
    cnt = 0
    
    # 원소에 대한 작업 반복 
    while True:
        # 다음 회차 arr 리스트 생성
        arr_next = []
        
        # arr 원소 작업
        for n in arr:
            if (n>=50) and (n%2==0):
                arr_next.append(n//2)
            elif (n<50) and (n%2!=0):
                arr_next.append(2*n + 1)
            else:
                arr_next.append(n)
        
        # arr과 arr_next가 같은지 확인
        if arr == arr_next:
            return cnt 
        
        else:
            cnt += 1
            arr = arr_next
        

    

'''
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
'''