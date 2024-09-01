def solution(s, n):
    answer = ''
    lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] * 2
    capital = [i.upper() for i in lower]
    
    for a in s:
        if a.islower() :
            idx = lower.index(a)
            idx+=n
            answer += lower[idx]
        elif a.isupper() :
            idx = capital.index(a)
            idx+=n
            answer += capital[idx]
        elif a == " ":
            answer += a

    return answer