# 단어 입력받기
arr = [input() for _ in range(5)]
# 입력 받은 단어를 세로로 나열하기
answer = ''.join(w[i] for i in range(max(map(len, arr))) for w in arr if i < len(w))
# 출력
print(answer)