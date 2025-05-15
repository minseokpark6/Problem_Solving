# 방정식 풀이 함수 생성
def solve_linear_equation(a, b, c, d, e, f):
    # 판별식 (determinant)
    determinant = a * e - b * d
    
    # # 해가 존재하지 않을 때
    # if determinant == 0:
    #     return "해가 없거나 무수히 많습니다."
    
    # x와 y 값 계산
    x = int((c * e - b * f) / determinant)
    y = int((a * f - c * d) / determinant)
    
    return x, y

# 입력 
a, b, c, d, e, f = map(int, input().split())
# x, y 구하기 
x, y = solve_linear_equation(a, b, c, d, e, f)
# 출력
print(x, y)