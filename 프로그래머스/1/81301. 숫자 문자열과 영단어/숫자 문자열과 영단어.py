def solution(s):
    # 변수 정의 
    word_list = ["zero", "one", "two", "three", 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    # 단어를 숫자로 변경 
    for i, w in enumerate(word_list):
        s = s.replace(w, str(i))
    
    # 출력 
    return int(s)

'''
(1) 불필요한 리스트 및 딕셔너리 삭제 


## 기존 통과 코드 

def solution(s):
    # 리스트 및 딕셔너리 정의 
    word_list = ["zero", "one", "two", "three", 'four', 'five', 'six', 'seven', 'eight', 'nine'] 
    num_list = [str(i) for i in range(10)]
    dic = {w:n for w, n in zip(word_list, num_list)}

    # 단어를 숫자로 변경 
    for w, n in dic.items():
        s = s.replace(w, n)
    # 출력
    return int(s)
'''