
# Create an explicit polynomial equation for z_r(t)
# from the Gale terrain CSV file

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import data from csv
data = pd.read_csv("gale_terrain_synthetic.csv")

# columns for time and height
time_values = np.array(data["time_s"])
height_values = np.array(data["elevation_m"])

# make polynomial curve
# input polynomial order
poly_order = 6

# retun coefficients
poly_coeff = np.polyfit(time_values, height_values, poly_order)

# turn the coefficients into a callable polynomial object
z_r = np.poly1d(poly_coeff)

# display equation
print("\nApproximation for mars terrain profile z_r(t):\n")
print(z_r)

# to display polynomial neatly
print("\nPolynomial coefficients (a0 is constant term):")
for i, c in enumerate(poly_coeff[::-1]):
    print(f"a{i} = {c:.6e}")

# data plot against polynomial
# dnese time axis to smoothen curve 
t_plot = np.linspace(time_values.min(), time_values.max(), 800)

plt.figure(figsize=(8,4))
plt.scatter(time_values, height_values, s=12, color="black", label="Recorded data")
plt.plot(t_plot, z_r(t_plot), "r-", lw=1.8, label=f"Polynomial line (deg={poly_order})")
plt.xlabel("Time [s]")
plt.ylabel("Height [m]")
plt.title("Polynomial Curve of Mars Terrain z_r(t)")
plt.grid(True, ls="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()
