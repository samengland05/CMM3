#Here is the work from tutorial. Root findinig using the secant method so maybe this is useful
import numpy as np
import matplotlib.pyplot as plt

fx=lambda x:x**2+4*x-12

def secant(f, x0,x1, N):
    for _ in range(N):
        fx0,fx1=f(x0), fx(1)
        if fx1-fx0 ==0:
            return None
        x2=x1-fx1*(x1-x0)/(fx1-fx0)
        x0,x1=x1,x2
    return x1

x0,x1=0,4

N_values=range(1,11)
xroots_secant=[]
errors_secant=[]

for N in N_values:
    xroot=secant(fx,x0,x1,N)
    xroots_secant.append(xroot)
    errors_secant.append(abs(fx(xroot)))

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.plot(N_values, xroots_secant, 'o-', label='Root estimate')
plt.xlabel('Iterations (N)')
plt.ylabel('x_root')
plt.title('Secant Method Root vs Iterations')
plt.grid(True)

plt.subplot(1,2,2)
plt.semilogy(N_values, errors_secant, 's-', color='r', label='|f(x_root)|')
plt.xlabel('Iterations (N)')
plt.ylabel('Error (log scale)')
plt.title('Secant Method Error vs Iterations')
plt.grid(True)
plt.tight_layout()
plt.show()

print("Final estimated root (Secant):", xroots_secant[-1])

