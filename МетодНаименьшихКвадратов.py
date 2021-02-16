import numpy as np

i = 0
x = [0] * 5
x[0] = 0
x[1] = 1
x[2] = 2
x[3] = 4
x[4] = 5
y = np.zeros(5)
y[0] = 2.1
y[1] = 2.4
y[2] = 2.6
y[3] = 2.8
y[4] = 3.0
n = int(input('¬ведите количество переменных i= '))
while i < n:
    a = (n*(x[i]*y[i]) - (x[i])*y[i]) / (n * (x[i]**2) - (x[i]**2))
    b = y[i] - (a * x[i]) / n
    f = [0] * 5
    f[i] = (y[i] - a * x[i] + b)**2
    print('значение f =', f[i], 'при а =', a, 'и b =', b)
    i += 1


