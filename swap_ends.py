def swap_ends(L, k):
    ### Replace with your own code (begin) ###
    n=len(L)
    if k<=0 or n==0 or k>n//2:
        return (L.copy(), 0)
    new_list=L.copy()
    new_list[:k], new_list[-k:]=L[-k:], L[:k]
    return(new_list, k)
    ### Replace with your own code (end)   ###
