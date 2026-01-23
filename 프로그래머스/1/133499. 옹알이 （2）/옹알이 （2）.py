# 순차 탐색 버전
def solution(babbling):
    # 변수 정의
    words = ["aya", "ye", "woo", "ma"]
    cnt = 0
    
    # 발음 가능한 단어 개수 카운트 
    for b in babbling:
        # 단어 비교를 위한 변수 정의
        prev = ""       # 중복 단어 방지 
        i = 0           # 단어의 index
        valid = True    # 발음 가능한 단어인지 여부 
        
        # 주어진 단어가 발음 가능한 단어인지 여부 
        while i < len(b):
            matched = False
            
            for w in words:
                if b.startswith(w, i) and w != prev:
                    matched = True 
                    prev = w 
                    i += len(w)
                    break
            
            if not matched:
                valid = False 
                break 
        
        if valid:
            cnt += 1
    
    # 출력 
    return cnt


'''
## 기존 replace 방식 유지 개선 코드 

def solution(babbling):
    # 변수 정의 
    words = ["aya", "ye", "woo", "ma"]
    cant = ["ayaaya", "yeye", "woowoo", "mama"]
    cnt = 0
    
    # 발음 가능한 단어 카운트 
    for b in babbling:
        word = b
        
        for c in cant:
            if c in word:
                word = 'x'
                break
        
        if word == 'x':
            continue 
        
        for w in words:
            word = word.replace(w, " ")
        
        if word.strip() == "":
            cnt += 1
        
    
    # 출력
    return cnt 

## 개선점 
(1) 입력 리스트의 직접 변경 X
(2) 불필요한 replace 최소화 


## 이전 코드

def solution(babbling):
    # 변수 설정
    words = ["aya", "ye", "woo", "ma"]
    cant = ["ayaaya", "yeye", "woowoo", "mama"]

    # 발음 가능한 단어 변경
    for i in range(len(babbling)):
        # 연속으로 오는 word는 변경 불가능
        for c in cant:
            babbling[i] = babbling[i].replace(c, "x")

        # 발음 가능한 단어는 " "로 치환
        for word in words:
            babbling[i] = babbling[i].replace(word, " ")

        # 카운팅을 위해 " "를 ""로 치환
        babbling[i] = babbling[i].replace(" ", "")
    
    # 출력
    return babbling.count("")

'''