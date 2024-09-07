def get_permutations(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_list_int32
    """
    def create_permutations(tmp, vals, len_required):
        if len(tmp) == len_required:
            res.append(tmp[:])
        else:
            for val in vals:
                tmp.append(val)
                new_vals = [x for x in vals if x != val]
                ## print(val, new_vals, tmp)
                create_permutations(tmp, new_vals, len_required)
                tmp.pop()
        return res
    res = []
    return create_permutations([], arr, len(arr)) if arr else []