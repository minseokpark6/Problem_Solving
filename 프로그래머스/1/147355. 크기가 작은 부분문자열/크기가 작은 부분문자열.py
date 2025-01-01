def solution(t, p):
    result = [int(t[i:i+len(p)]) for i in range(len(t)-len(p)+1) if int(p) >= int(t[i:i+len(p)])]
    return len(result)