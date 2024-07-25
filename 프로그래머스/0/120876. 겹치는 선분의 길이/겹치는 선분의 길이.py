def solution(lines):
    # 빈 집합 생성
    answer = set()
    
    for idx, a in enumerate(lines):
        for b in lines[idx+1 :]:
            answer |= set(range(a[0], a[1])) & set(range(b[0], b[1]))
            # |= : 집합에 다른 집합의 원소를 추가하는 연산자
            # range(a[0], a[1]) >> 점의 개수로 길이를 나타내기 때문에 선분 전체의 점이 나오지 않아야 함 
            # set(range(a[0], a[1])) & set(range(b[0], b[1])) >> 겹치는 부분의 길이를 점의 개수로 표현 
            
    return len(answer)