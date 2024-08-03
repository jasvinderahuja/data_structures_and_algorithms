#!/usr/bin/env python

def merge(L=[1,3,6,8], R=[1,2,3,4]):
    LR = []
    while L and R:
        if L[0] == R[0]:
            LR.append(L.pop(0))
            LR.append(R.pop(0))
        elif L[0] < R[0]:
            LR.append(L.pop(0))
        elif L[0] > R[0]:
            LR.append(R.pop(0))
    LR.extend(L)
    LR.extend(R)
    return LR

def merge_sort(arr=[1,3,1,4,2,6,6,7,7,8,5,2]):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        L_arr = merge_sort(arr[mid:])
        R_arr = merge_sort(arr[:mid])
    return merge(L_arr, R_arr)