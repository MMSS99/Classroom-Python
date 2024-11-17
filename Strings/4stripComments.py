# https://www.codewars.com/kata/51c8e37cee245da6b40000bd/
# \t inserta un tabulador.

def strip_comments(comment, markers):
    commentLines = comment.split('\n')

    modComment = []
    for line in commentLines:
        modLine = line

        for marker in markers:
            if marker in modLine:
                modLine = (modLine[:(modLine.index(marker))])

        try:
            while modLine[-1] == ' ' or modLine[-1] == '\t':
                modLine = modLine[:-1]
        except(IndexError):
            print(modLine)

        modComment.append(modLine)

    return '\n'.join(modComment)




if __name__ == "__main__":
    assert strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']) == 'apples, pears\ngrapes\nbananas'
    assert strip_comments('a #b\nc\nd $e f g', ['#', '$']) == 'a\nc\nd'
    assert strip_comments(' a #b\nc\nd $e f g', ['#', '$']) == ' a\nc\nd'