## Need to code this in under 10 minutes!
"""
Pseudocode:
    function helper(Pivot, start, end)
        ## leaf worker
        if start >= end:
            do nothing
            return
        
        ## Recursive: Internal code worker
        p_index = a random number in [start...end]
        swap A[p_index], A[start]
        left=start
        for right i.e, start+1 to end:
    ## Okay need to do this again!!
    ## use Lomuto's partitioning -- need to learn ##
    ## i.e., sort in place.
    ## In QuickSort values = pivot should be clubbed with pivot?
"""

def QuickSort(arr):
    if len(arr) <= 1:
        return(arr)
    else:
        import random
        pivot = random.choice(arr)
        n_pivot_repeats = 0
        l_arr = []
        s_arr = []
    

        for x in arr:
            if x == pivot:
                n_pivot_repeats+= 1
            elif x < pivot:
                l_arr.append(x)
            elif x > pivot:
                s_arr.append(x)
        
        return QuickSort(l_arr)+[pivot]*n_pivot_repeats+QuickSort(s_arr)
    