e = float(0.000001)
k = int(0)
x1 = float(input('Введите начальное х1= '))
x2 = float(input('Введите начальное х2= '))
x3 = float(input('Введите начальное х3= '))
while True:
    x11 = (9 - x2 - x3) / 4
    x22 = (10 - x11 + x3) / 6
    x33 = (20 - x11 - (2 * x22)) / 5
    if float(abs(x11-x1) < e) and float(abs(x22-x2)) < e and float(abs(x33-x3)) < e:
        break
    else:
        x1 = x11
        x2 = x22
        x3 = x33
        k += 1

print('Answer x1= ' + str(x11))
print('Answer x2= ' + str(x22))
print('Answer x3= ' + str(x33))
print('Iterasion k= ' + str(k))


