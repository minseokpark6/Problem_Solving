from itertools import product 

def solution(word):
    # 알파벳 모음으로 만들 수 있는 단어 리스트 생성 
    letters = ['A', 'E', 'I', 'O', 'U'] 
    word_list = sorted(["".join(c) for length in range(1, 6) for c in product(letters, repeat=length)])
    
    # 출력 
    return word_list.index(word) + 1

'''


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