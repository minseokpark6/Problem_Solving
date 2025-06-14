import sys 
input= sys.stdin.readline

# 함수 지정
def recursion(s, l, r, cnt):
    cnt += 1
    if l >= r: return 1, cnt
    elif s[l] != s[r]: return 0, cnt
    else: return recursion(s, l+1, r-1, cnt)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 0)

# 입력 
n = int(input().strip())
# 출력
for _ in range(n):
    cha = input().strip()
    result, cnt =isPalindrome(cha)
    print(result, cnt)