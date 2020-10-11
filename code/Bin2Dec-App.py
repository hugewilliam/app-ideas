# Projects/1-Beginner/Bin2Dec-App.md
import re
from utils import expecation

TYPE_ERROR = 'type error!'
INVALID_ERROR = 'invalid'
OVERFLOW_ERROR = 'stack overflow'


def bin2Dec(bin):
    if type(bin) != str:
        return TYPE_ERROR
    elif re.match('^[0-1]+$', bin) == None:
        return INVALID_ERROR
    elif len(bin) > 8:
        return OVERFLOW_ERROR

    match = 0
    base = 0
    for b in bin[::-1]:
        match += int(b) * 2**base
        base += 1

    return match


# test

int2 = lambda num: int(num, base=2)

expecation(bin2Dec(1011), TYPE_ERROR, 'input error type')
expecation(bin2Dec('101110111'), OVERFLOW_ERROR, 'input over 8 binary digits')
expecation(bin2Dec('1234'), INVALID_ERROR, 'input other than 0 or 1')
expecation(bin2Dec('100'), int2('100'), 'input 100 than result equal 4?')
expecation(bin2Dec('1011'), int2('1011'), 'input 1011 than result equal 11?')
