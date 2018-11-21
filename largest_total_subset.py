def get_largest_subset (num):     

    begin = end = None
    sav_begin = sav_end = None

    # curr_total : Tracks the current subset's total (including the negatives encountered at the tail).
    # sav_total  : Tracks the previous subset's total
    # be_total   : Tracks the total from begin index to end index (excluding the negatives encoutered at the tail)
    sav_total = be_total = None
    curr_total = 0

    # If true, start hunting for the next postive number.
    find_next_positive = True

    def do_save ():
        nonlocal sav_total, sav_begin, sav_end
        if  sav_total is None or be_total > sav_total:
            sav_total = be_total
            sav_begin = begin
            sav_end   = end  

    def do_save_neg (i, x):
        nonlocal sav_total, sav_begin, sav_end, be_total       
        if sav_total is None or x > sav_total:
            sav_total = be_total = x
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
            # Take 'x' in as the result is still positive (even if 'x' is negative)
            curr_total = curr_total + x
            # Only if 'x' is positive, we move the end hence update the begin-to-end total.
            if x > 0:
                be_total = curr_total
                end = i
            elif x < 0:
                do_save ()     
            print ('Begin={0} End={1} BE_Total={2} CurrTotal={3} SavTotal={4}'.format(begin, end, be_total, curr_total, sav_total))
        else:
            # Adding x has just made curr_total go negative or zero. The current quest ends here. 
            # Time to start finding a new subset
            # First, record if be_subset is greater sav_total
            do_save ()
            print ('Begin={0} End={1} BE_Total={2} CurrTotal={3} SavTotal={4}'.format(begin, end, be_total, curr_total, sav_total))
        
            # Time to reset stuff
            find_next_positive = True
            begin = end = None
            be_total = curr_total = 0

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