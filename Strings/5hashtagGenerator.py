#https://www.codewars.com/kata/52449b062fb80683ec000024/python

def generate_hashtag(s):
    hashtagCreator = s.split()
    hashtag = '#'
    for word in hashtagCreator:
        word = word.lower()
        word = word.capitalize()
        hashtag += word
    return hashtag if len(hashtag) > 1 and len(hashtag) < 141 else False

if __name__ == '__main__':
    assert(generate_hashtag('CoDeWaRs is niCe')) == '#CodewarsIsNice'

    assert(generate_hashtag('Codewars')) == '#Codewars'
    assert(generate_hashtag('Codewars      ')) == '#Codewars'
    assert(generate_hashtag('      Codewars')) == '#Codewars'
    assert(generate_hashtag('Codewars Is Nice')) == '#CodewarsIsNice'
    assert(generate_hashtag('codewars is nice')) == '#CodewarsIsNice'
    assert(generate_hashtag('CoDeWaRs is niCe')) == '#CodewarsIsNice'
    assert(generate_hashtag('c i n')) == '#CIN'
    assert(generate_hashtag('codewars  is  nice')) == '#CodewarsIsNice'
        
    #("Should return False if the input is empty, or result is longer than 140 chars")
    assert(generate_hashtag('') == False)
    assert(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat')) == False
               