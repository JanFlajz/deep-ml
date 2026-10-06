def label_encode_ordinal(values: list, order: list) -> list:
    """
    Encode ordinal categorical values to integers based on specified order.
    
    Args:
        values: List of categorical values to encode
        order: List specifying the order of categories from lowest (0) to highest
    
    Returns:
        List of integers representing the encoded values
    """
    d = {}
    for i,v in enumerate(order):
        d[v] = i
    d["unknown"] = -1
    res = []
    for i,v in enumerate(values):
        res.append(d[v])
    return res