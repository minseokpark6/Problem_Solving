def solution(s):
    # 변수 정의
    answer = []
    
    # 주어진 문자열을 리스트로 전처리 후 원소의 개수 별로 오름차순 정렬
    sorted_s = sorted([i.split(',') for i in s[2:-2].split('},{')], key=len)
    
    # 튜플에 담기 
    for i in sorted_s:
        for n in i:
            if n not in answer:
                answer.append(n)

    # 숫자로 변경 후 출력
    return [int(i) for i in answer]