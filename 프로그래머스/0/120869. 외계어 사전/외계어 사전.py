def solution(spell, dic):
    answer = 2
    spell_copied = spell.copy()

    for word in dic:
        spell_copied = spell.copy()
        for i in word:
            if i in spell_copied:
                word = word.replace(i, '')
                spell_copied.remove(i)
        if len(spell_copied) == 0:
            answer = 1

    return answer