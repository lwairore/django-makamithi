import re

_INTEGER_REGEX = '^[0-9]*$'

_FLOAT_REGEX = '^[0-9\.]*$'

INTEGER_TYPE = 'int'

FLOAT_TYPE = 'float'


def is_integer(value):
    return bool(re.match(_INTEGER_REGEX, value))


def is_float(value):
    return bool(re.match(_FLOAT_REGEX, value))
