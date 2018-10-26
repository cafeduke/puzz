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
    A number with fewer digits is considered to be greater than the one with fewer digits. Eg: 7 > 78, 789 < 800, 9 > 800 
    
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
    na, nb = len(a), len(b)

    # If the number of digits are same, comparision is same as string comparision (MSB to LSB)
    if na == nb:
        return cmp (a, b)

    # Slice the strings to min of the two lengths, and compare them. In essence, we are not using the extra portion of the larger string for the comparison.
    ln = min (na, nb)
    val = cmp(a[:ln], b[:ln])

    # A 'val' of 0  indicates larger string starts with same digits as smaller (like '78' and ''78965'). Return smaller string to be higher.
    # If a = '78' and b = '78965' then nb - na == 5 - 2 == 3. A positive value indicates a > b (as expected)
    return nb - na if val == 0 else val

def main ():
    l = [78, 789, 9, 998, 989, 0]
    print ("Input : ", l)
    l.sort(key=functools.cmp_to_key(cmp_large), reverse=True)    
    print ("Sort  : ", l)
    print ("Num   : ", seq(l).make_string(''))

if __name__ == '__main__':
    main ()
