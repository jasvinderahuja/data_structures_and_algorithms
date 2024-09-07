# Generate Binary Strings Of Length N
def get_binary_strings(n):
    """
    Args:
     n(int32)
    Returns:
     list_str
    """
    # Write your code here.
    def extend_string(tmp, res_string, len_n = n):
        len_res = len(tmp)
        if len_res == n:
            res_string = res_string.append(tmp[:])
        else:
            extend_string(tmp+"1", res_string, n)
            extend_string(tmp+"0", res_string, n)

        return res_string
    
    return [] if n==0 else extend_string("", [], n)