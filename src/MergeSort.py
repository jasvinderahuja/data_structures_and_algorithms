#!/usr/bin/env python
class MergeSort:
## All Merge based algos have the same structure
## WORKS: mid=(start+end)/2
## PERFECT (avoids overflow): mid = start+(end-start)/2 -- in case of in-place method
## for in-place we need to change: split2leaf_merge2build
## now use start:mid, mid+1:end
## otherwise 2 element array will be a problem! :)
## for below A = arr[start:mid], and B = arr[mid+1:end]
## For - MergeSort - we need STABILITY

"""
## Intuition -

sorted_merge function:
     merges two sorted lists
split2leaf_merge2build function:
    recursively splits to leaf elements
    finally merges all peices recursively using the merge function

-- need to learn to do it in place
"""

    def sorted_merge(L,R):
        print(f'L={L} and R={R}')
        LR=[]
        i=0
        j=0
        max_l = len(L)-1
        max_r = len(R)-1
        while i <= max_l and j <= max_r:
            if L[i] == R[j]:
                LR = LR+[L[i],R[j]]
                i+=1
                j+=1
            elif L[i] > R[j]:
                LR.append(R[j])
                j+=1
            elif L[i] < R[j]:
                LR.append(L[i])
                i+=1
        if i <= max_l:
            LR.extend(L[i:])
        if j <= max_r:
            LR.extend(R[j:])

        return LR

    def split2leaf_merge2build(arr):
        ## this is not in place ##
        len_A = len(arr)
        if len_A <= 1:
            return arr
        else:
            arr_mid = len_A//2
            L = split2leaf_merge2build(arr[:arr_mid])
            R = split2leaf_merge2build(arr[arr_mid:])
        return sorted_merge(L,R)

    def main():

    processor = MergeSort()
    processor.split2leaf_merge2build()

    if __name__ == "__main__":
        split2leaf_merge2build()