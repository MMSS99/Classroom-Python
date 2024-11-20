def anagrams(word, words):
    
    # comprensión de diccionario
    return ([anagrama for anagrama in words if ({char:word.count(char) for char in word}) == ({char:anagrama.count(char) for char in anagrama})])

    # comprensión de lista
    return [anagrama for anagrama in words if sorted(anagrama) == sorted(word)]

    # original
    '''
    anagrams = []
    for i in words:
        if ''.join(sorted(word)) == ''.join(sorted(i)):
            anagrams.append(i)
    return anagrams
    '''
    





if __name__ == "__main__":
    assert anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada', 'abbb', 'aaab']) == ['aabb', 'bbaa']
    assert anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) == ['carer', 'racer']
    assert anagrams('laser', ['lazing', 'lazy', 'lacer']) == []
    assert anagrams('a', ['a', 'b', 'c', 'd']) == ['a']
    assert anagrams('big', ['gig', 'dib', 'bid', 'biig']) == []
    assert anagrams('ab', ['cc', 'ac', 'bc', 'cd', 'ab', 'ba', 'racar', 'caers', 'racer']) == ['ab', 'ba']
    assert anagrams('abba', ['a', 'b', 'c', 'd', 'aabb', 'bbaa', 'abab', 'baba', 'baab', 'abcd', 'abbba', 'baaab', 'abbab', 'abbaa', 'babaa']) == ['aabb', 'bbaa', 'abab', 'baba', 'baab']
