#!/usr/bin/env python
## intersect two sorted arrays 
## Brutus and Caesar
## no aux space

## BruteForce O m(log n) 
## preferably n > m

# Alternatively,
## two, pointer O(max(m,n))
"""
i=0
j=0

while i<len(A) and j<length(B):
    if A[i] == B[j]:
        result.add(A[i])
        i++
        j++

    else if A[i] < B[j]:
        i++

    else A[i] > B[j]:
        j++

return result

## this is like - Merge Phase of MergeSort

"""