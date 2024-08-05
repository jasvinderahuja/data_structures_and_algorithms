def tower_of_hanoi(n):
    """
    Args:
     n(int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    res=[]
    def MoveDisk(nDisks, curr_site, target_site, aux_site):
        if nDisks == 1:
            # print([curr_site,target_site])
            # print(res)
            res.append([curr_site,target_site])
        else:
            ## move all other disks from curr_site to aux (see aux is target)
            MoveDisk(nDisks-1, curr_site, aux_site, target_site)
            
            res.append([curr_site,target_site])
            # print([curr_site,target_site])
            # print(res)
            
            ## move all other disks back from aux to target (see aux is target)
            MoveDisk(nDisks-1, aux_site, target_site, curr_site)
            
    ## n = nDisks, current_site=1, target=3, aux=2
    
    MoveDisk(n, 1,3,2)
    return res