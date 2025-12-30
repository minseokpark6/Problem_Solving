def solution(s):
    # 변수 정의
    result = []
    seen = set()
    sorted_str = sorted([i.split(',') for i in s[2:-2].split('},{')], key=len) 
    
    # 튜플에 담기
    for t in sorted_str:
        for i in t :
            if i not in seen:
                seen.add(i)
                result.append(int(i))
    
    # 출력
    return result


'''
## 개선점
(1) 해시 기반 자료구조인 set을 사용해서 'not in' 성능 개선
- O(N²) >> O(N)



## 기존 통과 코드 

def solution(s):
    # 변수 정의
    answer = []
    
    # 주어진 문자열을 리스트로 전처리 후 원소의 개수 별로 오름차순 정렬
    sorted_s = sorted([i.split(',') for i in s[2:-2].split('},{')], key=len)
    
    # 튜플에 담기 
    answer = []
    for i in sorted_s:
        for n in i:
            if n not in answer:
                answer.append(n)

    # 숫자로 변경 후 출력
    return [int(i) for i in answer]

'''