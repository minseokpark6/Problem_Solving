def solution(seoul):
    # 김서방 위치 저장
    idx = seoul.index("Kim")
    # 출력
    return f"김서방은 {idx}에 있다"


''' 
- 딕셔너리나 추가 리스트를 사용하는 것이 오히려 메모리 낭비 
- 이럴 경우엔 위의 코드처럼 바로 index를 사용하여 저정하는 것이 효율적 

def solution(seoul):
    dic = {name:idx for idx, name in enumerate(seoul) if name == "Kim"}
    return f'감서방은 {dic["Kim"]}에 있다'
'''