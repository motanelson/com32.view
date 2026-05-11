def limits(number,down,up):
    if number > up:
        return up,True
    if number < down:
        return down,True
    return number,False


b=0
c=False
for a in range(-8,18):
    b,c=limits(a,0,10)
    print(str(b)+" = " +str(c))