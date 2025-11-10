import numpy as np
import matplotlib.pyplot as plt

#This is the function that we look at. The maximum displacement of the system body subjected to the terrain
def max_displacement(k):
    def f(t,y):
        x, v =y
        a=(F(t)-c*v-k*x)/m 
        return np.array([v,a])
    #This integrates the ODE code into my function so it represents the system
    t, y=rk4(f, np.array([0.0,0.0]),0.0, 5.0, 0.001)
    x, _=y.T
    return np.max(np.abs(x))


#This allows for the value we are after to be the root so we can use root finding
def objective(k):
    return max_displacement(k)-0.025


def secant(f,x0,x1,tol=1e-6, N=50):
    for i in range(N):
        f0,f1=f(x0), f(x1)
        if f1-f0==0:
            print ("Division by 0 encountered")
            return None
        x2=x1-f1*(x1-x0)/(f1-f0)
        print(f"Iteration {i+1}:k={x2:.2f},f(k)={f(x2):.6f}")
        if abs(x2-x1)<tol:
            print("Convergred!")
            return x2
        x0,x1=x1,x2
    print("Did not converge within max iterations.")
    return x2

m=50
c=700
F=lambda t: 100*np.sin(2*np.pi*t)

k0,k1=2000,5000
k_solution= secant(objective,k0,k1)

print(f"\nEstimated stiffness k ≈ {k_solution:.2f} N/m")

