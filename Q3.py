# student number:2098580

def function_renamer(code):
    ''' Function that processes python code and renames function names, turning them into camel case

    Parameters
    ----------
    code: str

    Returns
    ----------
    tuple(d, newcode)
        d: dict
            d is a nested dictionary where each key corresponds to the original function name, it contains:
                hash: int, str, float
                    hash code of the original function name
                camalcase: str
                    camalcase version of the original function name
                allcaps: str
                    all caps version of the original function name
        newcode: str
            updated version of code with the camelcase function names
    '''
    # import necessary module
    import re
    regex = re.findall(r'def (.*?)\(', code) #finds the function name
    list_func = []
    # for loop to iterate over the list regex (i will be the index of the list)
    for i in range(len(regex)):
        new_string = ''
        j = 0
        while j != len(regex[i]):
            if regex[i][j] == '_': # if the index j points to an underscore
                # if the function starts with _
                if j == 0:
                    # finds all underscores at the beginning of the word
                    underscores = re.findall(r'\b_+', regex[i])
                    # adds them to the empty string
                    new_string += underscores[0]
                    # adds the capitilized letter after the underscores
                    new_string += regex[i][j + len(underscores[0])].upper()
                    j += 1 + len(underscores[0])
                # if the function has a _ as a space. the letter after becomes capitalized.
                else:
                    # finds all underscores in word (not at the beginning)
                    underscores = re.findall(r'_+', regex[i])
                    # the letter after the underscores is capitilized and added to the string
                    new_string += regex[i][j + len(underscores[0])].upper()
                    j += 1 + len(underscores[0])
            # if letter is a letter or number
            elif re.findall(r'[a-zA-Z0-9]', regex[i][j]):
                if j == 0:
                    # Make letter capital letter
                    new_string += regex[i][j].upper()
                    j += 1
                else:
                    # Add to string letter can be capital or lower case
                    new_string += regex[i][j]
                    j += 1
        # add the new function name to a list
        list_func.append(new_string)
    code_list = [code]
    d = {}
    # gets the answer in the form in the question
    for k in range(len(list_func)):
        code_list.append(re.sub(regex[k], list_func[k], code_list[k]))
        d[regex[k]] = {'hash': hash(regex[k]), 'camelcase': list_func[k],
                        'allcaps': regex[k].upper()}
    newcode = code_list[k + 1]
    return tuple((d, newcode))



### --- IMPORTANT: DO NOT REMOVE OR CHANGE THE CODE BELOW ---
if __name__ == '__main__':
    # Example 1
    testcases = {
        'example 1':
"""
def add_two_numbers(a, b):
  return a + b

print(add_two_numbers(10, 20))
""",
    'example 2' :
"""
def _major_split(*args):
  return (args[:2], args[2:])

def CheckTruth(t = True):
  print('t is', t)
  return _major_split([t]*10)

x, y = _major_split((10, 20, 30, 40, 50))
CheckTruth(len(x) == 10)
"""
    }
    for key, code in testcases.items():
        print(f'--- {key} ---')
        out = function_renamer(code)
        if not isinstance(out, tuple) or len(out)!=2:
            raise TypeError('function_renamer should return a tuple of length 2')
        d, newcode = out
        if not isinstance(d, dict):
            raise TypeError('return argument d should be a dictionary')
        if not isinstance(newcode, str):
            raise TypeError('return argument code should be a string')
        print('d = ', d)
        print('\ncode:')
        print(newcode)
