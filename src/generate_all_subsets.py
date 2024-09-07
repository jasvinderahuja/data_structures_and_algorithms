def generate_all_subsets(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    def get_subsets(tmp, res, len_s, strs):
        ## print(tmp)
        res.add(tmp[:])
        if len(tmp) <= len_s:
            for char in strs:
                strs = [x for x in strs if x != char]
                get_subsets(tmp+char, res, len_s, strs)
        return res
    res = set()
    len_s = len(s)
    return [""] if len_s == 0 else list(get_subsets("", res, len_s, s))