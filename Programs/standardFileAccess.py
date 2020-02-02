def safer_float(object):
    try:
        return_value = float(object)  
    except (ValueError, TypeError) :
        return_value = "The argument must be a numeric string or a number"
    else:
        print("There were no exceptions raised!")
    return return_value