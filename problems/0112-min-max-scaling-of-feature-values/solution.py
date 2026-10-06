def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    mx = max(x)
    mn = min(x)
    res =[]
    for i in x:
        res.append((i-mn)/(mx-mn))
    return res