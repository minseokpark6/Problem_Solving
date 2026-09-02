def solution(arr, k):
    # 변수 정의
    result = []

    # 중복되는 수 제외
    for i in arr:
        if i not in result:
            result.append(i)

    # 출력   
    return result if len(result) == k else result[:k] if len(result)>k else result + [-1]*(k-(len(result)))


'''
def solution(arr, k):
    # arr에서 중복되는 수 제외하고 answer에 담기
    answer = []
    for n in arr:
        if len(answer) == 0:
            answer.append(n)
        else:
            if n not in answer:
                answer.append(n)
                
    # k개의 개수만큼 뽑기
    if len(answer) == k:
        return answer
    elif len(answer) < k:
        while len(answer) < k:
            answer.append(-1)
    else:
        answer = answer[:k]
        
    return answer

arr = list(set(arr))

집합으로 중복제거를 할 경우 오름차순 정렬이 자동으로 됨
'''