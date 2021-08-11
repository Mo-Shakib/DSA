def midCircular(cir, start, size):
    # first and second largest no. index
    fl, sl = -1, -1
    # first and second smallest no. index
    fs, ss = -1, -1
    
    i = start
    cnt = 0
    length = len(cir)
    while cnt < size:
        if cir[i] % 2 == 1:
            i = (i+1)%length
            cnt = cnt + 1
            #ignore ods
            continue
        if fl == -1:
            fl = i
        elif cir[i] > cir[fl]:
            sl = fl
            fl = i
        elif sl == -1 or (sl != -1 and cir[i] > cir[sl]):
            sl = i
        
        if fs == -1:
            fs = i
        elif cir[i] < cir[fs]:
            ss = fs
            fs = i
        elif ss == -1 or (ss != -1 and cir[i] < cir[ss]):
            ss = i
        i = (i+1)%length
        cnt = cnt + 1
        
    print("Second Largest Even = {}".format(cir[sl]))
    print("Second Smallest Even = {}".format(cir[ss]))
    
    slVal = cir[sl]
    ssVal = cir[ss]
    # set next index of second largest odd
    cir[(sl+1)%length] = slVal + ssVal
    # set previous index
    prevIdx = ss-1
    if prevIdx < 0:
        prevIdx += length
    cir[prevIdx] = slVal * ssVal
    for i in range(length):
        print(cir[i], end=' ')
    print()

midCircular([44, 59, 0, 0, 0, 0, 10, 14, 4, 21], 6, 6)
midCircular([1, -2, -6, 0, 5, 6, 7, 12], 4, 7)