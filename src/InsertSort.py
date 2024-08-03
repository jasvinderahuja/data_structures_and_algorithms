#!/usr/bin/env python
def InsertSort(tArr):
    """
    pseudocode: 
    for each item in array
    move to the left till the item on left is not smaller than itself
    """
    len_tArr = len(tArr)
    for i in reversed(range(len_tArr)):
        for j in range(i):
            if tArr[i] < tArr[j]:
                tArr[i], tArr[j] = tArr[j], tArr[i]
    return tArr