def solution(a, b):
    # 금요일부터 시작한 요일 리스트 생성
    day_name = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    # 각 월별 전체 일수를 담은 리스트 생성
    month_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # 1월 1일부터 a월 b일까지의 일자 계산
    days = (sum(month_day[:a-1]) + (b-1))
    
    # 요일 출력
    return day_name[days%7]

'''

## 이전 통과 코드

def solution(a, b):
    # 금요일부터 시작한 요일 리스트 생성
    day_name = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    # 각 월별 전체 일수를 담은 리스트 생성
    month_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 1월 1일 > a월 b일까지의 "일"수를 담을 변수 생성
    day = 0
    
    # 1월 1일로부터 a월 1일까지의 day 수 
    for idx in range(a-1):
        day += month_day[idx]
    
    # + a월 1일부터 a월 b일 까지의 day 수
    day += (b-1)
    
    # 요일 구하기 
    day_idx = day % 7
    answer = day_name[day_idx]
    
    return answer

'''
    