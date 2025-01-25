from itertools import product

def solution(word):
    # 다섯가지 모음으로 만들 수 있는 길이 5 이하의 모든 단어 리스트
    letters = ['A', 'E', 'I', 'O', 'U']
    result = [''.join(comb) for length in range(1, 6) for comb in product(letters, repeat=length)]
    
    # 해당 단어의 인덱스 찾기
    idx = sorted(result).index(word)
    
    # 출력
    return idx+1