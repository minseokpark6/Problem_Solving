def solution(arr1, arr2):
    # 첫 번째 조건 길이 비교
    if len(arr1) != len(arr2):
        return 1 if len(arr1) > len(arr2) else -1
    
    # 두 번째 조건 합 비교
    if sum(arr1) != sum(arr2):
        return 1 if sum(arr1) > sum(arr2) else -1
    
    # 두 배열의 길이와 합이 같은 경우 
    return 0
        
'''
def solution(arr1, arr2):
    if len(arr1) < len(arr2):
        return -1
    elif len(arr1) > len(arr2):
        return 1
    else:
        if sum(arr1) < sum(arr2):
            return -1
        elif sum(arr1) > sum(arr2):
            return 1
        else:
            return 0
'''