def solution(code):
    mode = 0
    answer = ''
    # 반복문 
    for idx in range(len(code)):
        if mode == 0 :
            if code[idx] != "1":
                if idx % 2 == 0:
                    answer += code[idx]
            elif code[idx] == "1":
                mode = 1
    
        elif mode == 1 :
            
            if code[idx] != "1":
                if idx % 2 == 1:
                    answer += code[idx]
    
            elif code[idx] == "1":
                mode = 0
                
    if answer == "":
        return "EMPTY"
    else:
        return answer