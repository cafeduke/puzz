'''
Arrange a list of numbers such that the number resulting by joining them is the largest possible.
'''

import functools
from functional import seq

def cmp (a, b):
    ''' 
    Compare objects that can be converted to string
    
    Parameters
    ----------
    a : Object that can be converted to string.
        First object to be compared

    b : Object that can be converted to string.
        Second object to be compared
    
    Returns
    -------
    integer
        Positive number : a > b
        Negative number : a < b
        Zero            : a == b
    '''
    a, b = str(a), str(b)
    return (a > b) - (a < b)

def cmp_large(a, b):
    '''
    Comparator to compare two integers based on most significant number (left most) first.
    A number with fewer digits is considered to be greater than the one with fewer digits. 
        Eg :  7 < 78  because   778 <   787
        Eg : 77 > 771 because 77771 > 77177
    
    Parameters
    ----------
    a : integer
        First integer to be compared

    b : integer
        Second integer to be compared
    
    Returns
    -------
    integer
        Positive number : a > b
        Negative number : a < b
        Zero            : a == b
    '''
    a, b = str(a), str(b)
    return cmp (a+b, b+a)

def main ():
    l = [78, 789, 9, 998, 989, 0]
    print ("Input : ", l)
    l.sort(key=functools.cmp_to_key(cmp_large), reverse=True)    
    print ("Sort  : ", l)
    print ("Num   : ", seq(l).make_string(''))

if __name__ == '__main__':
    main ()
