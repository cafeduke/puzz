def get_largest_subset (num):     

    begin = end = None
    sav_begin = sav_end = None

    # sav_total  : Tracks the previous subset's total
    sav_total = None

    # curr_total : Tracks the current subset's total (including the negatives encountered at the tail).
    curr_total = 0

    # If true, start hunting for the next postive number.
    find_next_positive = True

    def do_save ():
        ''' record if begin-end-subset is greater than the saved one '''
        nonlocal sav_total, sav_begin, sav_end
        if  sav_total is None or curr_total > sav_total:
            sav_total = curr_total
            sav_begin = begin
            sav_end   = end  

    def do_save_neg (i, x):
        ''' if nothing is saved and 'x' is negative, save the largest 'x'. Index of 'x' shall be the begin and end '''
        nonlocal sav_total, sav_begin, sav_end
        if sav_total is None or x > sav_total:
            sav_total = x
            sav_begin = sav_end  = i

    for i, x in enumerate(num):

        print('')
        print ('{0}) {1}'.format(i, x))

        # Go until we find the next positive number
        if find_next_positive:
            # Num is negative/zero, so check the next one
            if x <= 0:
                do_save_neg(i, x)
                continue
            # Found the positive number, this is where we begin. Record the index.
            find_next_positive = False
            begin = i
        
        # Adding x to curr total still keeps it positive
        if curr_total + x >= 0:
            if x < 0:
                do_save ()
            curr_total = curr_total + x
            end = i
            print ('Begin={0} End={1} CurrTotal={2} SavTotal={3}'.format(begin, end, curr_total, sav_total))
        else:
            # Adding x has just made curr_total go negative or zero. The current quest ends here. 
            # Time to start finding a new subset
            # First, record if begin-end-subset is greater than the saved one.
            do_save ()
            print ('Begin={0} End={1} CurrTotal={2} SavTotal={3}'.format(begin, end, curr_total, sav_total))
        
            # Time to reset stuff
            find_next_positive = True
            begin = end = None
            curr_total = 0
    
    if sav_total > 0:
        do_save()

    return sav_begin, sav_end


if __name__ == '__main__':
    # num = [-5, 6, -3, 10, -1, -3, -8, -2, -4, 20, 20, 20, 20, 20, -2, -3, 40, 40]
    # num = [5, -3, 5, 5, 5, -6, 1, -3, 1, -3, 1, -3, 1]
    num = [-100, -10, -1, -1, -2, -2, -8]
    begin, end = get_largest_subset (num)
    print ('')    
    print ('-' * 80)
    print ("Begin={0} End={1} Set={2}, Total={3}".format(begin, end, num[begin:end+1], sum(num[begin:end+1])))
    print ('-' * 80)    