def sum(arg):
    total = 0
    try :
        isinstance(arg, int)
    except:
        TypeError
    for val in arg:
        total += val
    return total