def shift_num(num):
    ''' Return a string
    if num < 10 make it 10
    if num % 10 == 0 add 5
    else get rid of the num at the unit's digit
    '''
    num = int(num)
    if (num < 10):
        num = 10
    elif (num % 10 == 0):
        num += 5
    else:
        num = num // 10 * 10
    return str(num)