def solution(ineq, eq, n, m):
    # 조건 정의 
    condition = {
        ">=" : n>=m,
        "<=" : n<=m,
        ">!" : n>m,
        "<!" : n<m
    }
    
    # 출력
    return 1 if condition[ineq+eq] else 0
    
'''
def solution(ineq, eq, n, m):
    if ineq == "<" and eq == "=":
        result = (n <= m)
    elif ineq == ">" and eq == "=":
        result = (n >= m)
    elif ineq == "<" and eq == "!":
        result = (n < m)
    else:
        result = (n > m)
    
    if result == True:
        return 1
    else:
        return 0

'''
