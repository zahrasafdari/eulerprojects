zarayeb5 = []
zarayeb3 = []
zarayeb3va5=[]
total_list=[]

for num in range(1, 1000):
    if num % 5 == 0 and num % 5 < 1000 and num%3 !=0:
        zarayeb5.append(num)
    
    if num % 3 == 0 and num % 5 < 1000 and num%5 !=0:
        zarayeb3.append(num)
    
    if num%3==0 and num%5==0:
        zarayeb3va5.append(num)

for z in zarayeb5:
    total_list.append(z)

for z in zarayeb3:
    total_list.append(z)

for z in zarayeb3va5:
    total_list.append(z)

print(sum(total_list))


vmess://eyJhZGQiOiI5Mi4xMTkuNTYuMjQiLCJhaWQiOiIwIiwiaG9zdCI6ImFtdC5jb20iLCJpZCI6IjA1MmVmOTVlLTMzNzktNDU1Mi1mYmU1LTRiYjU5NTg2YzQ3NyIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwicG9ydCI6IjI1NTMyIiwicHMiOiJ4b3hvLWlyYW5jZWxsIiwic2N5IjoiYXV0byIsInNuaSI6IiIsInRscyI6Im5vbmUiLCJ0eXBlIjoiaHR0cCIsInYiOiIyIn0=
