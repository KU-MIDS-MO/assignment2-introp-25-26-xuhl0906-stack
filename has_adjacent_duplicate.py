def has_adjacent_duplicate(L):
    ### Replace with your own code (begin) ###
    for i in range(0, len(L)-1, 1):
        if L[i]==L[i+1]:
            return True
    return False
    ### Replace with your own code (end)   ###
