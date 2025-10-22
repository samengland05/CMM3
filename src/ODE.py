import numpy as np
import matplotlib.pyplot as plt

# Parameters (example Mars rover wheel suspension)
m = 50.0     # kg
k = 15000.0  # N/m
c = 1200.0   # N·s/m

# External force (terrain bump)
def F(t):
    return 1000.0 if 1.0 <= t <= 1.2 else 0.0

# ODE system: y = [x, v]  (displacement, velocity)
def f(t, y):
    x, v = y
    a = (F(t) - c*v - k*x) / m  # from m*a = F - c*v - k*x
    return np.array([v, a])

# Runge-Kutta 4th order
def rk4(f, y0, t0, tf, dt):
    t = np.arange(t0, tf + dt, dt)
    y = np.zeros((len(t), len(y0)))
    y[0] = y0
    for i in range(1, len(t)):
        k1 = f(t[i-1], y[i-1])
        k2 = f(t[i-1] + dt/2, y[i-1] + dt*k1/2)
        k3 = f(t[i-1] + dt/2, y[i-1] + dt*k2/2)
        k4 = f(t[i-1] + dt, y[i-1] + dt*k3)
        y[i] = y[i-1] + (dt/6)*(k1 + 2*k2 + 2*k3 + k4)
    return t, y

# Initial conditions
y0 = np.array([0.0, 0.0])  # x0=0, v0=0
t0, tf, dt = 0.0, 5.0, 0.001

# Solve
t, y = rk4(f, y0, t0, tf, dt)
x, v = y.T

# Plot displacement
plt.figure(figsize=(9,5))
plt.plot(t, x)
plt.title("Mars Rover Suspension (1D)")
plt.xlabel("Time [s]")
plt.ylabel("Displacement [m]")
plt.grid(True)
plt.show()

