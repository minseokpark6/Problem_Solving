# 입력 
s = input().strip()
# 부분 문자열(중복 제거)
arr = {s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)}
# 출력 
print(len(arr))