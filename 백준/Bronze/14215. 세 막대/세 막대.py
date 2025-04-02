# 입력
arr = sorted([int(i) for i in input().split()])
# 나무 막대로 구할 수 있는 가장 큰 둘레의 길이 
answer = arr[0]+arr[1]+min(arr[2], (arr[0]+arr[1]-1))
# 출력
print(answer)