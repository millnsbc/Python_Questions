#  student number:2098580

def pluralize(word):
    ''' Function that determines the plural of a word

    Parameters
    ----------
    word: str
        word to be pluralized

    Returns
    ----------
    dictionary: dict
        a dictionary which contains 'plural' : word_in_plural and 'status' : x
            where word_in_plural is the pluralized version of word
            and x is one of the following values: ‘empty_string’, ‘proper_noun’,
            ‘already_in_plural’, ‘success’.
    '''
    # import necessary module
    import re
    # read in proper_nouns file
    proper_nouns = open('proper_nouns.txt')
    dictionary = {}
    test = 0    # this is used to find words that do not fit the logic
    # if word is empty string
    if word == '':
        # adds to the empty dictionary the form wanted in the question
        dictionary['plural'] = ''
        dictionary['status'] = 'empty_string'
        test += 1
    # if word ends in an s
    elif word[-1] == 's':
        dictionary['plural'] = word
        dictionary['status'] = 'already_in_plural'
        test += 1
    # this for loop cycles through the proper_nouns file and finds if word is in the file
    for proper_noun in proper_nouns:
        # delete the new line
        proper_noun = proper_noun.strip('\n')
        # if proper_noun is a word in the proper_nouns file
        if proper_noun == word.lower():
            dictionary['plural'] = word
            dictionary['status'] = 'proper_noun'
            test += 1
    # If the word is not plural and is not a proper noun
    if test == 0:
        # if the word ends in a vowel
        vowel = re.findall(r'\w+[aeiou]\b', word)  # creates a list if the word ends in a vowel
        if vowel:
            if vowel[0] == word:
                word_in_plural = word + 's'
                dictionary['plural'] = word_in_plural
                dictionary['status'] = 'success'
                test += 1
        # if the word ends in y and is preceded by a constant
        y = re.findall(r'\w+[b-df-hj-np-tv-z]y\b', word)
        if y:
            if y[0] == word:
                word_in_plural = re.split(r'y\b', word)
                word_in_plural = word_in_plural[0] + 'ies'
                dictionary['plural'] = word_in_plural
                dictionary['status'] = 'success'
                test += 1
        # if the word ends in f
        f = re.findall(r'\w+f\b', word)
        if f:
            if f[0] == word:
                # deletes the f
                word_in_plural = re.split(r'f\b', word)
                # replaces with ves on the end of word
                word_in_plural = word_in_plural[0] + 'ves'
                dictionary['plural'] = word_in_plural
                dictionary['status'] = 'success'
                test += 1
        # if the word ends in sh, ch or z
        shchz = re.findall(r'\w+sh|\w+ch|\w+z\b', word)
        if shchz:
            if shchz[0] == word:
                # adds es to the end of the word
                word_in_plural = shchz[0] + 'es'
                dictionary['plural'] = word_in_plural
                dictionary['status'] = 'success'
                test += 1
    # for the words that do not fit any of the above rules
    if test == 0:
        word_in_plural = word + 's'
        dictionary['plural'] = word_in_plural
        dictionary['status'] = 'success'
    return dictionary


### --- IMPORTANT: DO NOT REMOVE OR CHANGE THE CODE BELOW ---
TEST_CASES = """failure
food
Zulma
injury
elf
buzz
computers
PCs

highway
presentation
pouch
COVID-19
adam""".split('\n')

if __name__ == '__main__':

  for test_noun in TEST_CASES:

    print(test_noun,'-->',pluralize(test_noun))
    print('----')
