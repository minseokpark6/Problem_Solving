def solution(number, limit, power):
    # 기사 별 약수의 개수 저장
    attack = []
    for i in range(1, number+1):
        count = 0
        for j in range(1, int(i**0.5) +1):
            if j**2 == i:
                count+=1
                continue
                
            if i % j == 0:
                count+=2

        # 공격력 제한 수치 확인 후 리스트에 추가
        if count > limit:
            count = power
        attack.append(count)

    # 출력
    return sum(attack)


"""
약수를 구할 때 시간 복잡도를 줄이는 방법 
-> n의 약수를 구할 때 약수는 항상 짝지어 나온다는 것을 생각하면 
- 아래 실패한 방법의 시간 복잡도 : O(N)
- 위 방법의 시간 복잡도 :  O(N^(1/2))

"""


"""
# 시간초과 실패

def solution(number, limit, power):
    # 기사 별 약수의 개수 저장
    attack = []
    for i in range(1, number+1):
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count+=1

        # 공격력 제한 수치 확인 후 리스트에 추가
        if count > limit:
            count = power
        attack.append(count)

    # 출력
    return sum(attack)
"""