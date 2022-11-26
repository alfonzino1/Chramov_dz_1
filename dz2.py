from collections import Counter
from functools import reduce
from operator import or_, add

def sum_dct(*dicts):
    return dict_transformer(*dicts)

def max_dct(*dicts):
    return dict_transformer(*dicts, op=or_)

def dict_transformer(*dicts, op=add):
    return dict(reduce(lambda a, b: op(Counter(a), Counter(b)), dicts))