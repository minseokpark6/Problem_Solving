def solution(arr, delete_list):
    answer = []
    for num in arr:
        if num not in delete_list:
            answer.append(num)
    return answer



'''
# for문 내부에서 for문을 돌리는 대상 변수를 조작하고 있는 것이 가장 큰 문제

def solution(arr, delete_list):
    for num in arr:
        if num in delete_list:
            arr.remove(num)
    return arr

'''