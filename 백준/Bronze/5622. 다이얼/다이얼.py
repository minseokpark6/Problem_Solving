alphabet = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
dic = {s: k for k, a in enumerate(alphabet, start=2) for s in a}
word = input()
sec = 0
for s in word:
    sec += (dic[s]+1)
print(sec)