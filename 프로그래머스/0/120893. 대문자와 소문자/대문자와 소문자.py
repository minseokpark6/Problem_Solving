def solution(my_string):
    return "".join(
        c.upper() if c.islower() else c.lower() 
        for c in my_string
    )



'''
def solution(my_string):
    answer = my_string.swapcase()
    return answer
'''