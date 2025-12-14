def solution(citations):
    # 정렬
    citations.sort(reverse=True)
    
    # H-Index 찾기
    for i, c in enumerate(citations):
        if c < i+1:
            return i
    
    # 그 이외의 경우
    return len(citations)

'''
## 개선점 
(1) 정렬과 인덱스를 이용하여 시간 복잡도 개선
- 최대 O(n²) -> O(n log n)


## 이전 통과 코드 

def solution(citations):
    # 최초 h 값 정의 
    h = len(citations)
    
    # H-Index 찾기 
    while True:
        if sum(n >= h for n in citations) >= h:
            break
        else:
            h -= 1
    
    # 출력
    return h
'''