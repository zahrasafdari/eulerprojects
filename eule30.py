summ = 0
i = 10
while i < 1000000:
    digit_sum = 0
    j = list(str(i))
    for x in j:
        digit = int(x) ** 5
        digit_sum += digit
    if digit_sum == i:
        summ += i
        print(i)
    i += 1

