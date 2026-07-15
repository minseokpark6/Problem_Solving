def solution(s1, s2):
    return len(set(s1) & set(s2))


'''
## 개선점 
(1) 시간 복잡도 개선 
- 이중 for 문은 모든 리스트 원소를 다 돌아야함으로 비효율적
- 집합(set)을 이용해 리스트의 탐색 시간인 O(n)을 O(1)로 단축

def solution(s1, s2):
    answer = 0
    for i in s1:
        for j in s2:
            if i == j:
                answer += 1
    return answer
'''