import numpy as np
import matplotlib.pyplot as plt



def max_displacement(k):
    def f(t,y):
        x, v =y
        a=(F(t)-c*v-k*x)/m 
        return np.array([v,a])
    t, y=rk4(f, np.array([0.0,0.0]),0.0, 5.0, 0.001)
    x, _=y.T
    return np.max(np.abs(x))
    

def F(t):
    if 1.0<=t<=1.2:
        return 330.0*np.sin(np.pi*(t-1)/0.17)
    else: 
        return 0.0


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


m=185/6
c=1000


##This creates a range of k values to plot

k_values_plot = np.linspace(500, 10000, 100) 


# We use objective(k) which returns (deflection - 0.05)
objective_values = []
for k_val in k_values_plot:
    print(f"Plotting: Trying k={k_val:.0f}")
    objective_values.append(objective(k_val))

#Create the plot
plt.figure(figsize=(10, 6))
plt.plot(k_values_plot, objective_values, 'b-', label='objective(k) [Max Deflection - 0.05 m]')

# Add the target line (where objective = 0)
plt.axhline(y=0.0, color='r', linestyle='--', 
            label='Target (objective = 0)')

#Add labels and title
plt.xlabel('Spring Stiffness $k$ (N/m)')
plt.ylabel('Objective Function Output')
plt.title('Objective Function vs. Stiffness')
plt.legend()
plt.grid(True)
plt.savefig('objective_function_plot.png')

print("Plot 'objective_function_plot.png' saved.")
print("Look at this plot to find where the blue line crosses the red line.")
print("Use k-values on either side of that crossing as your new k0 and k1.")

k0,k1=4000,6000
k_solution= secant(objective,k0,k1)
print(f"\nEstimated stiffness k ≈ {k_solution:.2f} N/m")

