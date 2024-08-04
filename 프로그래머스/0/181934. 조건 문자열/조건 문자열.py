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
