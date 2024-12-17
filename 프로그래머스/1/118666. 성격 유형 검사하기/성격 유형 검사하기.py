# 딕셔너리 활용 코드
def solution(survey, choices):
    # 변수 지정
    answer = ''
    
    # 딕셔너리 생성
    scores = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    dic = {1: 3, 2: 2, 3: 1, 4: 0, 5: -1, 6: -2, 7: -3}
    
    # 점수 계산
    for i, c in enumerate(survey):
        key = choices[i]
        scores[c[0]] += dic[key] if key < 4 else 0  # 첫 번째 문자에 더하기
        scores[c[1]] += -dic[key] if key > 4 else 0  # 두 번째 문자에 빼기

        
    # 성격 유형 구하기(지표 번호 순서대로) 
    answer += 'R' if scores['R'] >= scores['T'] else 'T'
    answer += 'C' if scores['C'] >= scores['F'] else 'F'
    answer += 'J' if scores['J'] >= scores['M'] else 'M'
    answer += 'A' if scores['A'] >= scores['N'] else 'N'
    
    # 출력
    return answer

"""
# 파이썬 if -else 표현식 
- if-else 표현식 (삼항 연산자)은 값을 반환하는 표현식
- **AN +=**가 if문과 else문 양쪽에 동시에 쓰였기 때문에 문법적으로 맞지 않음
    - ex. AN += dic[key_] if c == "AN" else AN += -(dic[key_])
"""

"""
## 기존 코드
def solution(survey, choices):
    # 변수 지정
    answer = ''
    RT, CF, JM, AN = 0, 0, 0, 0
    
    # 성격 유형 앞 글자(알파벳순 정렬)를 기준으로 점수 딕셔너리 생성
    dic = {1:3, 2:2, 3:1, 4:0, 5:-1, 6:-2, 7:-3}
    
    # 각 성격 유형 별 점수 더하기 
    for i, c in enumerate(survey):
        key = choices[i]
        if c in ["RT", "TR"]:
            RT += dic[key] if c == "RT" else -(dic[key])
        elif c in ["CF", "FC"]:
            CF += dic[key] if c == "CF" else -(dic[key])
        elif c in ["JM", "MJ"]:
            JM += dic[key] if c == "JM" else -(dic[key])
        elif c in ["AN", "NA"]:
            AN += dic[key] if c == "AN" else -(dic[key])
    
    # 성격 유형 구하기 
    scores, category = [RT, CF, JM, AN], ["RT", "CF", "JM", "AN"]

    for idx, score in enumerate(scores):
        answer += category[idx][0] if score >= 0 else category[idx][1]
    
    # 출력
    return answer
"""