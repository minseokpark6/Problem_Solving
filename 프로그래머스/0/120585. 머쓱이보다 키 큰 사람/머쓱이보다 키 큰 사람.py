def solution(array, height):
    arr1 = []
    for i in range(len(array)):
        if array[i] > height:
            arr1.append(array[i])
            i += 1
    answer = len(arr1)
    return answer