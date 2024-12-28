def solution(s):
    # 리스트 및 딕셔너리 정의
    word_str = ["zero", "one", "two", "three", 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num_str = [str(i) for i in range(10)] 
    word_dic = {w:n for w, n in zip(word_str, num_str)}
    
    # 주어진 단어 숫자로 변경
    for w, n in word_dic.items():
        s = s.replace(w, n)
        
    # 출력
    return int(s)


"""
# 정답 

def solution(s):
    # 리스트 및 딕셔너리 정의
    word_str = ["zero", "one", "two", "three", 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num_str = [str(i) for i in range(10)] 
    word_dic = {w:n for w, n in zip(word_str, num_str)}
    
    # 주어진 단어 숫자로 변경
    answer, temp = "", ""
    for i in s:
        if i in num_str:
            answer += i
        else:
            temp += i
            if temp in word_str:
                answer += word_dic[temp]
                temp = ""
    # 출력
    return int(answer)
"""