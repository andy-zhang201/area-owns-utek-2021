def mergesort(arra):
    if len(arra)>1:
        middle = len(arra)//2
        LHS = mergesort(arra[:middle])
        RHS = mergesort(arra[middle:])

        l = 0
        r = 0
        i = 0
        new_arra = []

        while l < len(LHS) and r < len(RHS):
            if LHS[l][1] < RHS[r][1]:
                new_arra.append(LHS[l])
                l+=1
            else:
                new_arra.append(RHS[r])
                r+=1
            i+=1

        for x in LHS[l:]:
            new_arra.append(x)
        for y in RHS[r:]:
            new_arra.append(y)

    else:
        new_arra = arra[:]

    return new_arra


l = [('Path 1', 0.85), ('Path 2', 1.1764705882352942), ('Path 3', 0.7619047619047619)]
print(mergesort(l))