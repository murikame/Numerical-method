from math import sin

def work(f, a, b, n):
    print("\nТекущее число разбиений: ", n)
    h = (b - a) / float(n)
    print("Текущий шаг:", h)
    total = sum([f((a + (k * h))) for k in range(0, n)])
    result = h * total
    print("Текущий результат: ", result)
    return result

def f(x):
    return (-0.03 * x**(3) + 0.26 * x - 0.26)

n = 10
a = 1
b = 2
x = work(f, a, b, n)

print("\nОтвет:", x, "\nКоличество разбиений:", n)
#______________________________________________________________________________________________________________________
from math import sin
import numpy as np

def work(f, a, b, n):
    print("\nТекущее число разбиений: ", n)
    h = (b - a) / float(n)
    print("Текущий шаг:", h)
    total = sum([f((a + (k * h))) for k in range(0, n)])
    result = h * total
    print("Текущий результат: ", result)
    return result

def f(x):
    return (x**(2))*sin(x)

n = 10
a = (np.pi)/2
b = 3*np.pi
x = work(f, a, b, n)

print("\nОтвет:", x, "\nКоличество разбиений:", n)

#______________________________________________________________________________________________________________________
from math import sin
from math import cos
import numpy as np

def work(f, a, b, n):
    print("\nТекущее число разбиений: ", n)
    h = (b - a) / float(n)
    print("Текущий шаг:", h)
    total = sum([f((a + (k * h))) for k in range(0, n)])
    result = h * total
    print("Текущий результат: ", result)
    return result

def f(x):
    return np.e**(cos(x)**2)

n = 10
a = 0
b = 2*np.pi
x = work(f, a, b, n)

print("\nОтвет:", x, "\nКоличество разбиений:", n)

