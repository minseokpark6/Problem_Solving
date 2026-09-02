def solution(numbers):
    # 변수 정의
    nums = {"zero":"0", 
        "one":"1", 
        "two":"2", 
        "three":"3", 
        "four":"4", 
        "five":"5", 
        "six":"6", 
        "seven":"7", 
        "eight":"8", 
        "nine":"9"}
    # 정수로 변환
    for word, digit in nums.items():
        numbers = numbers.replace(word, digit)
        
    # 출력
    return int(numbers)


'''
def solution(numbers):
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for idx, num in enumerate(nums):
        numbers = numbers.replace(num, str(idx))
    return int(numbers)
'''