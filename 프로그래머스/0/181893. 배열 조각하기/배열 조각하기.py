def solution(arr, query):
    for idx, q in enumerate(query):
        if idx % 2 == 0:
            arr = arr[:q+1]
        else:
            arr = arr[q:]
    return arr