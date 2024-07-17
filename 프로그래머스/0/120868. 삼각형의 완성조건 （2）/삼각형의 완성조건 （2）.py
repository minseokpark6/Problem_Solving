def solution(sides):
    max_sides = max(sides)
    min_sides = min(sides)
    sum_sides = sides[0] + sides[1]
    # 나머지 한 변이 제일 긴 경우 
    temp_1 = list(range(max_sides+1, sum_sides))
    # sides에 제일 긴 변이 있는 경우
    temp_2 = list(range(max_sides - min_sides + 1, max_sides + 1))
    
    # answer 출력
    answer = len(list(set(temp_1 + temp_2)))
    return answer