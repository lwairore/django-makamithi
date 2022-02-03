from typing import Iterable


def iterable_object_is_not_empty(iterable_object: Iterable):
    if not isinstance(iterable_object, Iterable):
        return False

    return True if len(iterable_object) > 0 else False
