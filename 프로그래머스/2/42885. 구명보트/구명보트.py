def solution(people, limit):
    # 변수 정의
    answer = 0
    first = 0
    last = len(people) - 1
    
    # 몸무게 내림차순으로 정렬 
    people.sort(reverse = True)
    
    # 몸무게가 무거운 first와 가벼운 last의 합을 하나씩 limit과 비교 
    while first <= last:
        
        # 몸무게가 무거운 사람과 가벼운 사람의 합이 limit보다 작은 경우
        if people[first] + people[last] <= limit:
            last -= 1
    
        # 구명정 개수 추가, 다음 몸무게가 무거운 사람으로 한칸 이동
        answer += 1
        first += 1
        
    
    # 출력 
    return answer