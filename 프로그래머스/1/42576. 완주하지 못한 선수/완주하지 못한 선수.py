def solution(participant, completion):
    # 빈 딕셔너리 생성 
    dic = {}
    
    # 딕셔너리에 참가자 추가 
    for part in participant:
        dic[part] = dic.get(part, 0) + 1
        
    # 완주자 제거 
    for comple in completion:
        dic[comple] -= 1
    
    # 출력 
    for name, count in dic.items():
        if count == 1:
            return name
    



''' 기존 통과 코드 
def solution(participant, completion):
    # 빈 딕셔너리 생성
    dic = {}
    
    # 딕셔너리에 참가자 추가
    for part in participant:
        if part in dic:
            dic[part] += 1
        else:
            dic[part] = 1
    
    # 딕셔너리에서 완주한 사람 제외 
    for com in completion:
        dic[com] -= 1
    
    # 남아있는 사람 출력
    return ''.join([name for name in dic if dic[name] == 1])
'''

"""
# 위 코드와 아래 코드의 시간 복잡도의 차이 

## 성공 코드의 경우 
총 시간 복잡도:
딕셔너리의 평균 접근 시간은 **O(1)**이므로,

O(n + m + n) = O(n + m)
(여기서 m ≈ n - 1이므로 결국 **O(n)**로 간주할 수 있음)

## 실패 코드의 경우 
완주자 수가 m, 참가자 수가 n이라면, remove가 최대 n번의 탐색을 반복하므로:
최악의 경우 **O(m × n)**의 시간 복잡도가 발생

"""

"""
# 효율성 테스트 실패

def solution(participant, completion):
    for i in completion:
        if i in participant:
            participant.remove(i)

    return participant[0]
"""