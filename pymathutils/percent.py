def percentage(value, total):
    """
    Get the percentage % result of value / total
    """
    try:
        return int((value/float(total))*100)
    except ZeroDivisionError:
        return int(0)


def percent_value(value, total):
    """
    Gets the value of a percentage.
    """
    try:
        return int((value * float(total))/100)
    except ZeroDivisionError:
        return int(0)
