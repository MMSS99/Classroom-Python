def anagrams(word, words):
    return [anagrama for anagrama in words if sorted(anagrama) == sorted(word)]
    '''
    anagrams = []
    for i in words:
        if ''.join(sorted(word)) == ''.join(sorted(i)):
            anagrams.append(i)
    return anagrams
    '''
    #return [anagrama if sorted(anagrama) == sorted(word) for anagrama in words] # Pide ELSE?
    #return [anagrama for anagrama in words if sorted(anagrama) == sorted(word)]



if __name__ == "__main__":
    assert anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada', 'abbb', 'aaab']) == ['aabb', 'bbaa']
    assert anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) == ['carer', 'racer']
    assert anagrams('laser', ['lazing', 'lazy', 'lacer']) == []
    assert anagrams('a', ['a', 'b', 'c', 'd']) == ['a']
    assert anagrams('big', ['gig', 'dib', 'bid', 'biig']) == []
    assert anagrams('ab', ['cc', 'ac', 'bc', 'cd', 'ab', 'ba', 'racar', 'caers', 'racer']) == ['ab', 'ba']
    assert anagrams('abba', ['a', 'b', 'c', 'd', 'aabb', 'bbaa', 'abab', 'baba', 'baab', 'abcd', 'abbba', 'baaab', 'abbab', 'abbaa', 'babaa']) == ['aabb', 'bbaa', 'abab', 'baba', 'baab']
