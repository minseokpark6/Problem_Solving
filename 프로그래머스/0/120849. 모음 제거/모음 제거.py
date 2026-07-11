def solution(my_string):
    # 모음 리스트 정의
    vowel = ['a', 'e', 'i', 'o', 'u']
    # 출력
    return ''.join(i for i in my_string if i not in vowel)


'''
def solution(my_string):
    vowel = ['a', 'e', 'i', 'o', 'u']
    for v in vowel:
        my_string = my_string.replace(v, '')
    return my_string
'''