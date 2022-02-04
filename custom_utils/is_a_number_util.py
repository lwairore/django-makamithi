import re

_INTEGER_REGEX = '^[0-9]*$'

_FLOAT_REGEX = '^[0-9\.]*$'

INTEGER_TYPE = 'int'

FLOAT_TYPE = 'float'


def is_integer(value):
    return bool(re.match(_INTEGER_REGEX, value))


def is_float(value):
    return bool(re.match(_FLOAT_REGEX, value))


def is_a_number(value, number_type=INTEGER_TYPE):
    if type(value) != str:
        value = str(value)

    if number_type == INTEGER_TYPE:
        return is_integer(value)
    elif number_type == FLOAT_TYPE:
        return is_float(value)
    else:
        raise ValueError(
            'Value for argument \'number_type\' is not recognized.')
