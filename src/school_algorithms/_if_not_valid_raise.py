def _if_not_int_or_float_raise(*args):
    for arg in args:
        if type(arg) != int and type(arg) != float:
            raise ValueError ("At least one of the values wasn't an integer or a float.")

def _if_not_positive_raise(*args):
    for arg in args:
        if arg <= 0:
            raise ValueError ("At least one of the values wasn't a positive number.")
