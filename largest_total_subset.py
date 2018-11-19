num = [-5, 6, -3, 10, -1, -3, -8, -2, -4, 20, 20, 20, 20, 20, -2, -3, 40, 40]
# num = [-1, -2, 6, 1, 1, -4, -1, 10, -20, 1, 8, -60]
begin = end = None
sav_begin = sav_end = 0

# curr_total : Tracks the current subset's total (including the negatives encountered at the tail).
# sav_total : Tracks the previous subset's total
# be_total   : Tracks the total from begin index to end index (excluding the negatives encoutered at the tail)
sav_total = curr_total = be_total = 0

# If true, start hunting for the next postive number.
find_next_positive = True

for i, x in enumerate(num):

    print('')
    print ('{0}) {1}'.format(i, x))

    # Go until we find the next positive number
    if find_next_positive:
        # Num is negative, so check the next one
        if x <= 0:
            continue
        # Found the positive number, this is where be begin. Record the index.
        find_next_positive = False
        begin = i
    
    # Adding x to curr total still keeps it positive
    if curr_total + x >= 0:
        # Take 'x' in as the result is still positive (even if 'x' is negative)
        curr_total = curr_total + x
        if x > 0:
            be_total = curr_total
            end = i
        print ('Begin={0} End={1} BE_Total={2} Total={3} PrevTotal={4}'.format(begin, end, be_total, curr_total, sav_total))
        continue

    # Adding x has just made curr_total go negative or zero. The current quest ends here. 
    # Time to start finding a new subset

    # First, record if curr subset is greater than prev
    if be_total > sav_total:
        sav_total = be_total
        sav_begin = begin
        sav_end   = end
    print ('Begin={0} End={1} BE_Total={2} Total={3} PrevTotal={4}'.format(begin, end, be_total, curr_total, sav_total))
    
    # Time to reset stuff
    find_next_positive = True
    begin = end = None
    be_total = curr_total = 0

if be_total > sav_total:
    sav_total = be_total
    sav_begin = begin
    sav_end   = end
    print ('Begin={0} End={1} BE_Total={2} Total={3} PrevTotal={4}'.format(begin, end, be_total, curr_total, sav_total))

print ('')    
print ('-' * 80)
print ("Begin={0} End={1} Total={2}".format(sav_begin, sav_end, sav_total))
print ('-' * 80)

