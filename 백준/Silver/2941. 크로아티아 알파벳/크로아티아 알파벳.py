word = input()
cro_word = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for w in cro_word:
    if w in word:
        word = word.replace(w, "*")
        
print(len(word))