#!/usr/bin/env python
def BubbleSort(tArr):
    """
    pseudocode:
    for length(tArr) times
        go from left to right
            swap(i-1,ith) elements if A[i] < A[i-1]    
    """
    len_tArr = len(tArr)
    for i in range(len_tArr):
      for j in range(1,len_tArr-i):
        ## print(f'i={i} and j={j}')
        if tArr[j-1] > tArr[j]:
            tArr[j-1], tArr[j] = tArr[j], tArr[j-1]
      ## print(tArr)
    return(tArr)