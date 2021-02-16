import numpy as np
file = open('Euler.txt', 'w')
file_2 = open('Analiti4eskoe.txt', 'w')
L = 1 #конечное значение х
n = 1001 #количество разбиений
x0 = 0 #начальное значение х
h = L / (n-1)
i = 0
x = [0] * n
y = [0] * n
x[0] = 0
y[0] = 1
def fun(x, y):
    f = 2 * ((x**2) + y)
    file_2.write(str(x) + ' ' + str(y))
    file_2.write('\n')
    return f
x = np.arange(x0, L, h)
while(1):
    y[i+1] = y[i] + (h * fun(x[i], y[i]))
    write_x = x[i]
    write_y = y[i+1]
    file.write(str(write_x) + ' ' + str(write_y))
    file.write('\n')
    if (x[i] > L):
        file.close()
        file_2.close()
        break
    else:
        i += 1