def find_fibonacci(n):
    """
    Args:
     n(int32)
    Returns:
     int32
    """
    arr = [0,1]
    
    for i in range(2,n+1):
        arr.append(arr[i-2]+arr[i-1])
        ## print(arr)
    return arr[n]