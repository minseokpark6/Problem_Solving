def solution(strings, n):
    return sorted(strings, key= lambda x : (x[n], x))

'''
### sorted()

(1) key = 
- key를 기준으로 정렬

(2) lambda x : (x[n], x)
- x[n]을 1순위로 놓고 정렬하고, 
- x[n]이 같은 경우, 2순위는 x로 정렬 

'''