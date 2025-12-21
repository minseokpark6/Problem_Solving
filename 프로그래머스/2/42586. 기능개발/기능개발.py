def solution(progresses, speeds):
    # 각 작업 별 완료일 정의 
    days = [(100-p)//s if (100-p)%s == 0 else (100-p)//s + 1 for p, s in zip(progresses, speeds)]

    # 배포일 별 기능 개수 카운트
    result = []
    current_day = days[0]
    cnt = 1

    for d in days[1:]:
        if d <= current_day:
            cnt += 1        
        else:
            result.append(cnt)
            current_day = d
            cnt = 1

    result.append(cnt)

    # 출력
    return result

'''

## 기존 코드 
def solution(progresses, speeds):
    # 각 작업 별 완료일 정의 
    dates = [(100-p)//s if (100-p)%s == 0 else (100-p)//s + 1 for p, s in zip(progresses, speeds)]

    # 배포일 별 기능 개수 카운트
    result, stk = [], []

    for d in dates:
        if not stk:
            stk.append(d)
            continue
        
        if stk[0] >= d:
            stk.append(d)
        else:
            result.append(len(stk))
            stk = []
            stk.append(d)

    result.append(len(stk))

    return result

'''
