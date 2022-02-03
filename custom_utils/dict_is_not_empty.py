from custom_utils.model_instance_is_an_instance_of_util import model_instance_is_an_instance_of


def dict_is_not_empty(dict_item):
    return model_instance_is_an_instance_of(dict_item,
                                            dict) and bool(dict_item)
