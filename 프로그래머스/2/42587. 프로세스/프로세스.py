def solution(priorities, location):
    # 변수 설정 
    answer = 0 
    # 우선 순위와 location 설정
    pr = [[idx, i] for idx, i in enumerate(priorities)]
    # priorities 내림차순 정렬 
    sorted_pr = sorted(priorities, reverse=True)
    
    
    # location의 실행 순서 
    while pr:
        temp = pr[0]
        pr.remove(temp)
        # 가장 큰 수 설정
        first = sorted_pr[0]
        
        if temp[1] != first:
            pr.append(temp)
            
        elif temp[1] == first:
            # location 확인
            if temp[0] == location:
                answer += 1
                break
            else:
                sorted_pr.remove(first)
                answer += 1
            

    # 출력
    return answer