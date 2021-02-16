import numpy as np
file_4 = open('RKM.txt', 'w')
L = 1 #конечное значение х
x0 = 0 #начальное значение х
e = 0.0000000001 #точность
n = 1001 #количество разбиений
h = L / (n-1)
i = 0
x = [0] * n
y = [0] * n
x[0] = 0
y[0] = 1
def fun(x, y):
    f = 2 * ((x ** 2) + y)
    return f
x = np.arange(x0, L, h)
while(1):
    k1 = (h / 3) * fun(x[i], y[i])
    k2 = (h / 3) * fun((x[i] + h / 3), (y[i] + k1))
    k3 = (h / 3) * fun((x[i] + h / 3), (y[i] + (k1 / 2) + (k2 / 2)))
    k4 = (h / 3) * fun((x[i] + h / 2), (y[i] + ((3 * k1) / 8) + ((9 * k3) / 8)))
    k5 = (h / 3) * fun((x[i] + h), (y[i] + ((3 * k1) / 2) - ((9 * k3) / 2) + (6 * k4)))
    e1 = (1 / 5) * (k1 + (4 * k4) - ((9 * k3) / 2) - (k5 / 2))
    if (e1 <= 5 * e):
        y[i+1] = y[i] + (1 / 2) * (k1 + 4 * k4 + k5)
        x[i+1] = x[i] + h
        write_x = x[i+1]
        write_y = y[i+1]
        file_4.write(str(write_x) + ' ' + str(write_y))
        file_4.write('\n')
        if(x[i+1] > L):
            file_4.close()
            break
        else:
            h = h * pow(abs(e / e1), 1/5)
            i += 1
            k1 = 0
            k2 = 0
            k3 = 0
            k4 = 0
            k5 = 0




