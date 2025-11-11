import numpy as np
import matplotlib.pyplot as plt

# Parameters (example Mars rover wheel suspension)
m = 50.0     # kg
k = 5413.71  # N/m
c = 400   # N·s/m

# External force (terrain bump)


# ODE system: y = [x, v]  (displacement, velocity)
def f(t, y):
    x, v = y
    y_t = terrain(t)          # terrain displacement at time t
    dy_dt = terrain_derivative(t)  # terrain velocity at time t
    a = (k*(y_t - x) + c*(dy_dt - v)) / m
    return np.array([v, a])

def terrain(t):
    return (-1.728e-17*(t**6) +
            1.02e-13*(t**5) -
            2.265e-10*(t**4) +
            2.336e-7*(t**3) -
            0.0001102*(t**2) +
            0.01905*t -
            0.1875)

def terrain_derivative(t):
    return (-1.728e-17*6*(t**5) +
             1.02e-13*5*(t**4) -
             2.265e-10*4*(t**3) +
             2.336e-7*3*(t**2) -
             0.0001102*2*t +
             0.01905)

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
t0, tf, dt = 0.0, 1000.0, 0.1

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
plt.xticks(np.arange(0, 1100, 100)) 
plt.show()
