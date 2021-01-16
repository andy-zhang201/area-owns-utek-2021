def mergesort(arra):
    middle = len(arra)//2
    LHS = mergesort(arra[:middle])
    RHS = mergesort(arra[middle+1:])

    l = 0
    r = 0
    i = 0
    new_arra = []

    while l < len(LHS) and r < len(RHS):
        if LHS[l]<RHS[r]:
            new_arra.append(LHS[l])
            l+=1
        else:
            new_arra.append(RHS[r])
            r+=1

    new_arra.append(LHS[l:],RHS[r:])

    return new_arra