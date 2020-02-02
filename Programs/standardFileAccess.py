def safer_float(object):
    try:
        return_value = float(object)  # return the object without changes
    except ValueError:
        return_value = "could not convert to float"
    except TypeError:
        return_value = "This type of cant be converted to a float"
    return return_value