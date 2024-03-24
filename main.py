def to_hms(seconds: int) -> list:
    """
    Converts seconds to hours, minutes, and seconds, and returns it as a list.

    Parameters
    ---------
    seconds: int
        the seconds to be calculated

    Returns
    ---------
    list
        a list of integers representing hours, minutes, seconds

    Example:
    >>> to_hms(10)
    [0, 0, 10]
    >>> to_hms(61)
    [0, 1, 1]
    >>> to_hms(7199)
    [1, 59, 59]
    """
    # Type your code below
    pass
    if isinstance(seconds, str):
       print("Unsupported input type.")
    else:
       mins, secs = divmod(seconds, 60)
       hrs, mins = divmod(mins, 60)
       list = [hrs, mins, secs]
       return list
