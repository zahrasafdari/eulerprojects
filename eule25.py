import math
math.factorial(1000)
i = 10
summ = 0
# facs=[]
while i < 10000000:
    facs = 0
    j = list(str(i))
    for x in j:
        numfac = math.factorial(int(x))
        facs += numfac
    if facs == i:
        summ += i
        print(summ)
    i += 1
    #     facs.append(numfac)
    # for fac in facs:
