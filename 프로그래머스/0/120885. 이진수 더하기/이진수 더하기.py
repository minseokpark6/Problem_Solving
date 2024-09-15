from operator import *

def solution(bin1, bin2):
    return bin(add(int(bin1,2), int(bin2,2)))[2:]



"""
1. int(bin1,2)
>> 2진수를 10진수 정수로 변환 
>> 2번 째 인수인 2는 이진수로 해석하라는 의미 

2. bin()
더한 결과를 다시 이진수로 변환 
>> 결과 값 : 0b로 시작하는 이진수 문자열을 반환

3. [2:]
0b를 제거하고 순수한 이진수 부분만 반환

"""