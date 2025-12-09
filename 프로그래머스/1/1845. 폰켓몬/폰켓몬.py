def solution(nums):
    # 출력
    return min(len(nums)//2, len(set(nums)))

'''
## 이전 통과 코드

def solution(nums):
    answer = 0
    pocketmon = set(nums)
    
    if len(pocketmon) >= (len(nums)//2):
        answer = (len(nums)//2)
    else:
        answer = len(pocketmon)
    
    return answer


'''