x01 = float(1)
x02 = float(-1)
x03 = float(1)
e = 0.00001
k = int(1)
i = 1
n = 3
A = [[2, -1, 1],
    [-1, 2, -1],
    [0, 0, 3]]

B = [[x01],
    [x02],
    [x03]]

while(1):    
    x11 = float(A[0][0]*x01+A[0][1]*x02+A[0][2]*x03)
    x22 = float(A[1][0]*x01+A[1][1]*x02+A[1][2]*x03)
    x33 = float(A[2][0]*x01+A[2][1]*x02+A[2][2]*x03)
    lamb01 = x11/x01
    lamb02 = x22/x02
    lamb03 = x33/x03
    x01 = x11
    x02 = x22
    x03 = x33
    s = x01
    x11 = float(A[0][0]*x01+A[0][1]*x02+A[0][2]*x03)
    x22 = float(A[1][0]*x01+A[1][1]*x02+A[1][2]*x03)
    x33 = float(A[2][0]*x01+A[2][1]*x02+A[2][2]*x03)
    lamb11 = x11/x01
    lamb22 = x22/x02
    lamb33 = x33/x03
    while i<=n:
        LambD2 = float((x11-lamb01*x01)/(x01-lamb01*s))
        i += 1
    if (abs(lamb11 - lamb01) < e and abs(lamb22 - lamb02) < e and abs(lamb33 - lamb03) < e):
        print('answer 1= ', lamb11)
        print('answer 2= ', lamb22)
        print('answer 3= ', lamb33)
        print('iteration= ', k)
        print('answer LAMB2= ', LambD2)
        break
    k += 1


