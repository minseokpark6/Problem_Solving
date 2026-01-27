def solution(word):
    # 변수 정의
    letters = ['A', 'E', 'I', 'O', 'U']     # 사전 순서로 정렬
    cnt = 0
    answer = 0
    
    # 완전 탐색 함수 정의
    def dfs(current):
        nonlocal cnt, answer    # 상위 함수에서 변수 가져오기
        
        if current:
            cnt += 1
            if current == word:
                answer = cnt
                # 답을 찾은 경우 해당 회차 함수 종료
                return 
        
        # 길이가 5인 경우 탐색 종료
        if len(current) == 5:
            return 
        
        for l in letters:
            dfs(current + l)
    
    # 재귀 함수 시작
    dfs("")

    # 출력
    return answer 

'''
## 개선점
(1) 재귀를 이용한 완전탐색(dfs) 방식으로 변경 
- 메모리 사용량이 적고, 
- 조건에 따라 가지치는 방식의 변경이 자유롭게 가능


## 이전 코드 
from itertools import product 

def solution(word):
    # 알파벳 모음으로 만들 수 있는 단어 리스트 생성 
    letters = ['A', 'E', 'I', 'O', 'U'] 
    word_list = sorted(["".join(c) for length in range(1, 6) for c in product(letters, repeat=length)])
    
    # 출력 
    return word_list.index(word) + 1


## 순열 / 조합

(1) 순열 permutations 
- 반복 허용 X 
- 순서 고려 O 
- (1, 2) (1, 3) (1, 4) (2, 1) (2, 3) (2, 4) (3, 1) (3, 2) (3, 4) (4, 1) (4, 2) (4, 3)

(2) 조합 combinations 
- 반복 허용 X 
- 순서 고려 X 
- (1, 2) (1, 3) (1, 4) (2, 3) (2, 4) (3, 4) 

(3) 중복 순열 product 
- 반복 허용 O
- 순서 고려 O 
- (1, 1) (1, 2) (1, 3) (1, 4) (2, 1) (2, 2) (2, 3) (2, 4) (3, 1) (3, 2) (3, 3) (3, 4) (4, 1) (4, 2) (4, 3) (4, 4)

(4) 중복 조합 combinations_with)_replacement
- 반복 허용 O 
- 순서 고려 X 
- (1, 1) (1, 2) (1, 3) (1, 4) (2, 2) (2, 3) (2, 4) (3, 3) (3, 4) (4, 4) 


'''
    