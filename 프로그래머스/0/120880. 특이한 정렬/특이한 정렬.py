def solution(numlist, n):
    return sorted(numlist, key = lambda x:(abs(n-x), n-x))


"""
# 1. sorted 함수 
sorted(리스트, key=정렬기준, reverse=내림차순 여부)


# 2. lambda
lambda 매개변수: 반환값


# 3. 정렬 기준  key = lambda
- lambda 함수의 결과값 (abs(n-x), n-x)이 정렬 기준
- 튜플 순서를 기반으로 정렬
    - 절대값을 기준으로 선 정렬
    - 절대값이 같을 경우, n-x 를 기준으로 정렬

"""