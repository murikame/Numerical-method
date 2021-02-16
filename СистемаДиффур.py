import numpy as np
file_1 = open('file1.txt', 'w')
file_2 = open('file2.txt', 'w')
x0 = float(input('Введите левую границу х = '))
L = float(input('Введите правую границу х = '))
n = 1001
e = float(input('Введите задаваемую точность е = '))
h = L / (n - 1)
x = 0
y1 = 0
y2 = 3

def fun1(x, y1):
    return (-2 * y1) + (4 * y2)

def fun2(x, y2):
    return (-y1) + (3 * y2)

while(1):
    k1_1 = (h / 3) * fun1(x,y1)
    k1_2 = (h / 3) * fun2(x,y2)
    k2_1 = (h / 3) * fun1(x + (h / 3), y1 + k1_1)
    k2_2 = (h / 3) * fun2(x + (h / 3), y2 + k1_2)
    k3_1 = (h / 3) * fun1(x + (h / 3), y1 + (k1_1 / 2) + (k2_1 / 2))
    k3_2 = (h / 3) * fun2(x + (h / 3), y2 + (k1_2 / 2) + (k2_2 / 2))
    k4_1 = (h / 3) * fun1(x + (h / 2), y1 + ((3 * k1_1) / 8) + ((9 * k3_1) / 8))
    k4_2 = (h / 3) * fun2(x + (h / 2), y2 + ((3 * k1_2) / 8) + ((9 * k3_2) / 8))
    k5_1 = (h / 3) * fun1(x + h, y1 + ((3 * k1_1) / 2) - ((9 * k3_1) / 2) + (6 * k4_1))
    k5_2 = (h / 3) * fun2(x + h, y2 + ((3 * k1_2) / 2) - ((9 * k3_2) / 2) + (6 * k4_2))
    e1 = (1 / 5) * (k1_1 + (4 * k4_1) - (9 * k3_1) - (k5_1 / 2))
    e2 = (1 / 5) * (k1_2 + (4 * k4_2) - (9 * k3_2) - (k5_2 / 2))
    if(e1 <= (5 * e) and e2 <= (5 * e)):
        y1 = y1 + ((1 / 2) * (k1_1 + (4 * k4_1) + k5_1))
        y2 = y2 + ((1 / 2) * (k1_2 + (4 * k4_2) + k5_2))
        x = x + h
        write_x = x
        write_y1 = y1
        write_y2 = y2
        file_1.write(str(write_x) + ' ' + str(write_y1))
        file_1.write('\n')
        file_2.write(str(write_x) + ' ' + str(write_y2))
        file_2.write('\n')
        if(x > L):
            file_1.close()
            file_2.close()
            break
        else:
            h = h * pow(abs(e / e1), 1 / 5)
            k1_1 = 0
            k1_2 = 0
            k2_1 = 0
            k2_2 = 0
            k3_1 = 0
            k3_2 = 0
            k4_1 = 0
            k4_2 = 0
            k5_1 = 0
            k5_2 = 0

