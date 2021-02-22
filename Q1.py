#  student number:2098580

def do_arithmetic(x, y, op=''):
    ''' Performs an operation on two numbers and returns the result.

    Parameters
    ----------
    x: int or float
        A number
    y: int or float
        A number
    op: str, optional
        represents an arithmetic operation. Takes the arguments:
        'add' to add x and y
        'subtract' to subtract y from x
        'divide' to divide x by y (note: if y=0 returns None)
        'multiply' to multiply x and y
        '' (blank) adds x and y

    Returns
    ----------
    answer: float
        the result of the equation
    None
        if trying to divide by 0 or unknown operation provided

    '''
    # if the operation is 'add'
    if op == 'add':
        # adds x and y
        answer = x+y
    # if the operation is 'subtract'
    elif op == 'subtract':
        # subtracts y from x
        answer = x-y
    # if the operation is 'multiply'
    elif op == 'multiply':
        # multiplies x and y
        answer = x*y
    # if the operation is 'divide'
    elif op == 'divide':
        # checks if it is dividing by 0
        if y != 0:
            # if not dividing by 0, divides x by y
            answer = x/y
        # if dividing by 0
        else:
            # return none
            answer = None
    # if no operation argument is given
    elif op == '':
        # adds x and y
        answer = x+y
    # if an unknown operation is given
    else:
        print('Unknown operation')
        answer = None
    return float(answer)


def sum_of_digits(s):
    ''' Takes a string with numbers. Outputs the sum of the individual numbers.

    Parameters
    ----------
    s: str
        string that contains numbers

    Returns
    ----------
    int
        the result of summing all numbers in s
        0 if s is not provided
        0 if s is provided with no integers
    '''
    # if s is blank
    if s == '':
        # return 0
        total = 0
    nums = [0] # list with 0 if s is not empty but does not contain numbers
    # cycles through each index of the string s
    for i in s:
        # if i is a number
        if i.isnumeric():
            # turn the number from string to int
            a = int(i)
            # add to the list
            nums.append(a)
    # sum all numbers in the list
    total = sum(nums)
    return(total)


### --- IMPORTANT: DO NOT REMOVE OR CHANGE THE CODE BELOW ---
if __name__ == '__main__':
    testcases = {'do_arithmetic': [(10, 4, 'add'), (2, 3, 'multiply')],
    'sum_of_digits':[("123",), ("10a20",)]}

    print('\n-- do_arithmetic testcases --')
    for args in testcases['do_arithmetic']:
        print('input:', str(args))
        print('output:', do_arithmetic(*args))
        print('-----------')

    print('\n-- sum_of_digits testcases --')
    for args in testcases['sum_of_digits']:
        print('input:', str(args))
        print('output:', sum_of_digits(*args))
        print('-----------')
