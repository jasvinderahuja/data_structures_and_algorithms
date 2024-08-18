def count_all_subsets(n):
    """
    Args:
     n(int32)
    Returns:
     int32
    """
    if n==0:
        return 1
    else:
        return 2 * count_all_subsets(n-1)