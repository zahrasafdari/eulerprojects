def summ(n,m):
    number=n**m
    the_sum=0
    numlist=list(str(number))
    for x in numlist:
        the_sum+=int(x)

    return the_sum

print(summ(2,10000))

