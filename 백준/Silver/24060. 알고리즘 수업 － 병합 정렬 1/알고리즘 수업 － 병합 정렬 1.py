# 문제 내 병합 정렬 의사 코드
cnt = 0
result = -1

def merge_sort(A, p, r):
    global cnt, result
    if p < r:
        q = (p + r) // 2        # q는 p와 r의 중간 지점
        merge_sort(A, p, q)     # 전반부 정렬
        merge_sort(A, q + 1, r) # 후반부 정렬
        merge(A, p, q, r)       # 병합

def merge(A, p, q, r):
    global cnt, result, K
    i = p
    j = q + 1
    tmp = []

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
    # 전반부 배열이 남은 경우
    while i <= q:
        tmp.append(A[i])
        i += 1
    # 후반부 배열이 남은 경우
    while j <= r:
        tmp.append(A[j])
        j += 1
    # K번째 저장되는 수 변수에 저장
    for t in range(len(tmp)):
        A[p + t] = tmp[t]
        cnt += 1
        if cnt == K:
            result = tmp[t]

# 입력 
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 함수 내 변수 정의
cnt = 0
result = -1

# 출력
merge_sort(A, 0, N-1)
print(result)