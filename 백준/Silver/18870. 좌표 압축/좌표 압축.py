# 입력
n = int(input())
arr = list(map(int, input().split()))
# 숫자 중복 제거 및 정렬
sorted_arr = sorted(set(arr))
# 좌표 압축 > 딕셔너리
dic = {v:i for i, v in enumerate(sorted_arr)}
# 출력
print(*[dic[k] for k in arr])