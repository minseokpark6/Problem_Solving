from datetime import datetime as dt 

def solution(today, terms, privacies):
    answer = []
    td = dt.strptime(today, "%Y.%m.%d")

    # 유효기간 딕셔너리로 변환
    dic = {}
    for i in terms:
        temp = list(map(str, i.split()))
        dic[temp[0]] = int(temp[1])

    for idx, i in enumerate(privacies):
        arr = list(map(str, i.split()))
        date, term = dt.strptime(arr[0], "%Y.%m.%d"), arr[1]
        # date_diff = [월, 일]
        date_diff = [(td.year-date.year)*12 + (td.month-date.month), (td.day-date.day)]
        # 날짜의 차이가 음수라면 월을 한 달 줄이고 날짜로 변환
        if date_diff[1] < 0:
            date_diff[0] -= 1
            date_diff[1] += 28
        # 날짜 차이와 유효기간 비교 
        if date_diff[0] >= dic[term]:
            answer.append(idx+1)

    return answer