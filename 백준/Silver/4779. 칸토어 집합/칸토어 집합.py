import sys 
input = sys.stdin.readline

# 칸토어 집합 함수
def cantor(n):
    if n == 1:
        return '-'
    
    cantor_unit = cantor(n//3)
    cantor_res = cantor_unit + " "*(n//3) + cantor_unit
    
    return cantor_res

# 출력 
while True:
    try:
        n = int(input())
        print(cantor(3**n))
    except:
        break