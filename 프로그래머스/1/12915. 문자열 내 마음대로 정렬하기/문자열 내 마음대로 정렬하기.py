def solution(strings, n):
    answer = sorted(strings, key = lambda x : (x[n], x))
    return answer

'''
(1) sorted()
strings를 sorted 한다 

(2) key 
key를 기준으로 sorted 해라. 

(3) lambda 
lambda 함수를 사용해서 
x[n]를 기준으로 하고, 
x[n]가 같을 경우, 그냥 x를 기준으로 해라 
-> 첫 번째 문자를 기준으로 sorted하겠다.

'''