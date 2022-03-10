from functools import reduce
numbers=[]
for num in range(1,101):
    numbers.append(num)
zarb = reduce(lambda x, y: x*y, numbers)
print(sum(map(int, str(zarb))))