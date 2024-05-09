def maxTrailing(levels):
    dict = {}
        
    for i in range(len(levels)):
        dict[levels[i]] = 0
        j = 0
        while j < i:
            x = levels[i] - levels[j]
            if dict[levels[i]] < x:
                dict[levels[i]] = x
            j += 1
    
    vals = dict.values()
    
    if min(vals) - max(vals) == 0:
        return -1
    
    else:
        return max(vals)

maxTrailing([7, 2, 3, 10, 2, 4, 8, 1])