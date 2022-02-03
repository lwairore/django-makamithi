def string_is_not_empty(value):
    value = str(value)
    
    return bool(value and not value.isspace() and value != 'null')
