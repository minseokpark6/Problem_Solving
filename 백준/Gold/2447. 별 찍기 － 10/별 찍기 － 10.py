# 재귀로 별 찍는 함수 생성
# "***"을 한 묶음으로 보는 것이 핵심
def recursion(n):
    if n == 1:
        return ['*']
    
    stars = recursion(n//3)
    arr = []
    
    for star in stars:
        arr.append(star*3)
    for star in stars:
        arr.append(star + " "*(n//3) + star)
    for star in stars:
        arr.append(star*3)
    
    return arr

# 입력
n = int(input())
# 출력
print('\n'.join(recursion(n)))