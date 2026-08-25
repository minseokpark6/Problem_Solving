def solution(before, after):
    return 1 if sorted(before)==sorted(after) else 0
    
'''
def solution(before, after):
    before = sorted(list(before))
    after = sorted(list(after))
    if before == after:
        return 1
    else :
        return 0
'''