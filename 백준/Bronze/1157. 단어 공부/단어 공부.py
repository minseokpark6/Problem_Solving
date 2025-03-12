word = input().upper()
word_list = list(set(word))
arr = []

for i in word_list:
    cnt = word.count(i)
    arr.append(cnt)

if arr.count(max(arr))>1:
    print("?")
else:
    print(word_list[arr.index(max(arr))])