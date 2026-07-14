def solution(array):
    # 인덱스 값을 포함하여 딕셔너리로 변환
    dic = {n:idx for idx, n in enumerate(array)}
    
    # 출력
    return list(sorted(dic.items(), reverse=True)[0])


'''
## 개선점 
- 딕셔너리를 활용한 시간 복잡도 개선 

def solution(array):
    max_num = array[0]
    answer = []
    
    for i in array:
        if max_num < i:
            max_num = i
            
    idx = array.index(max_num)
    
    answer.append(max_num)
    answer.append(idx)
    
    return answer
'''