def solution(arr, queries):
    for query in queries:
        i, j = query[0], query[1]
        a, b = arr[i], arr[j]
        arr[i] = b
        arr[j] = a
    return arr