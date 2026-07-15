def solution(array, height):
    return sum(1 for h in array if h > height)
'''
def solution(array, height):
    arr1 = []
    for i in range(len(array)):
        if array[i] > height:
            arr1.append(array[i])
            i += 1
    answer = len(arr1)
    return answer

'''