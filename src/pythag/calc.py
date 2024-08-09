def square(value: float) -> float:
    """Square a value

    Args:
        value (float): _description_

    Returns:
        float: _description_
    """
    return value**2

def sqrt(value):
    """_summary_

    Args:
        value (_type_): _description_

    Returns:
        _type_: _description_
    """
    return value**0.5

def pythag(opp, adj):
    """_summary_

    Args:
        opp (_type_): _description_
        adj (_type_): _description_
    """
    hypot = sqrt(square(opp) + square(adj))
    return(hypot)