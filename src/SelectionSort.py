#!/usr/bin/env python
def SelectionSort(tArr):
    """
    pseudocode:
    for every position in array
    choose the smallest number and swap position with the current resident of that position
    """
    len_tArr = len(tArr)
    for i in range(len_tArr):
        swapper = i
        for j in range((i+1),len_tArr):
            ## print(f'i={i} and j={j}')
            if tArr[swapper] > tArr[j]:
                swapper = j
        tArr[i],tArr[swapper] = tArr[swapper],tArr[i]
        print(tArr)
    return tArr