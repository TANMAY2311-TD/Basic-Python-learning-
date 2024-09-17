good_condition = True
reasonable_price = False
poor_foundation = False

if good_condition and reasonable_price:   #both will be true
    print('I will buy the house.')

if good_condition or reasonable_price:   #any of them true
    print('I am interested.')

if good_condition and not poor_foundation:  #either any of them will be true
    print('It is a good deal!')
