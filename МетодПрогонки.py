n = 3
a = [0, 2, 2, 3]
b = [5, 4.6, 3.6, 4.4]
c = [-1, -1, -8.8, 8]
d = [2.0, 3.3, 2.6, 7.2]

A = [0] * 4
B = [0] * 4

i = 1
while i<=n:
    A[0] = -c[i]/b[i]
    B[0] = d[i]/b[i]
    A[i] = -c[i]/(b[i]+a[i]*A[i-1])
    B[i] = (d[i]-a[i]*B[i-1])/(b[i]+a[i]*A[i-1])
    i += 1
    
i = 1
x = [0] * 4
while n>=i:
    x[n] = (d[n]-a[n]*B[n-1])/(b[n]+a[n]*A[n-1])
    
    print(x[n])
    n -= 1

x[1] = a[1]*x[2]+B[1]
print(x[1])


