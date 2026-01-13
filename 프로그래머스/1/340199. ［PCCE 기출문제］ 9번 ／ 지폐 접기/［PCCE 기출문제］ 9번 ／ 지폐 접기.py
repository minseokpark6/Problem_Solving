def solution(wallet, bill):
    # 변수 정의 
    cnt = 0 
    
    # 정렬을 통해 정리 
    wallet.sort()
    bill.sort()
    
    # 최소 횟수 카운트 
    while (bill[0] > wallet[0]) or (bill[1] > wallet[1]):
        bill[1] //= 2   # 항상 긴 변
        bill.sort()
        cnt += 1
    
    # 출력
    return cnt

'''
## 이전 통과 코드 

def solution(wallet, bill):
    answer = 0
    while min(bill)>min(wallet) or max(bill)>max(wallet) :
        if bill[0] > bill[1]:
            bill[0] = bill[0]//2
        else:
            bill[1] = bill[1]//2
        answer += 1
    return answer
'''