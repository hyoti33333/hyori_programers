def solution(spell, dic):
    spell_key = ''.join(sorted(spell))
    
    for word in dic:
        if ''.join(sorted(word)) == spell_key:
            return 1
    return 2
